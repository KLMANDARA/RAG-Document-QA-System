# Military RAG Q&A System

A command-line Retrieval-Augmented Generation (RAG) system that allows users to interact with military mission documents using LLMs like Mistral or DeepSeek.

## How It Works

1. Loads mission documents from `data/`
2. Splits documents into chunks
3. Uses FAISS for semantic search
4. Uses an LLM to generate human-like answers

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```
