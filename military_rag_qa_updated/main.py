from utils.loader import load_documents
from models.rag_model import RAGModel

def main():
    print(" Military Document Question and Answer.")
    docs = load_documents("data/mission1.txt")
    rag = RAGModel(docs)

    while True:
        q = input("\nAsk a question on Military Document (or type 'exit'): ")
        if q.lower() == 'exit':
            break
        answer = rag.query(q)
        print(f"\nAnswer:\n{answer}\n")

if __name__ == "__main__":
    main()
