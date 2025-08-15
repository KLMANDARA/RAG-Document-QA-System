def load_documents(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    chunks = content.split("\n\n")
    return [chunk.strip() for chunk in chunks if chunk.strip()]
