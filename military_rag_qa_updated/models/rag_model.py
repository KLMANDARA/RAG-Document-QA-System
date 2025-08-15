from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

class RAGModel:
    def __init__(self, docs, embedding_model='all-MiniLM-L6-v2', llm_model='google/flan-t5-base'):
        self.docs = docs
        self.embedding_model = SentenceTransformer(embedding_model)
        self.embeddings = self.embedding_model.encode(docs)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        self.llm = pipeline("text2text-generation", model=llm_model, tokenizer=llm_model, max_new_tokens=512)

    def query(self, question, top_k=1):
        # Step 1: Search top_k relevant documents
        q_embed = self.embedding_model.encode([question])
        _, indices = self.index.search(q_embed, top_k)
        context = "\n".join([self.docs[i] for i in indices[0]])

        # Step 2: Construct prompt (and truncate if needed)
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        if len(prompt) > 2048:  # Truncate long prompts
            prompt = prompt[:2048]

        # Step 3: Generate answer
        output = self.llm(prompt)[0]["generated_text"]

        # Step 4: Extract clean answer (after "Answer:")
        if "Answer:" in output:
            return output.split("Answer:")[-1].strip()
        else:
            return output.strip()
