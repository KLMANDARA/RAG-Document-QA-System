# RAG-based Document QA System (DRDO Internship) ![Python](https://img.shields.io/badge/python-3.8+-blue) ![LangChain](https://img.shields.io/badge/langchain-compatible-brightgreen) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

This is a command-line based Retrieval-Augmented Generation (RAG) system designed to answer questions over structured military documents.

## ✨ Features
- Uses **FAISS** for vector search over document embeddings
- Integrates **open-source LLMs** (e.g., LLaMA, DeepSeek)
- Modular implementation using **LangChain**
- Supports context-aware Q&A from structured PDFs

## 🖼️ Screenshots
> _Coming soon: You can add screenshots or CLI demo GIFs here_  
![screenshot-placeholder](https://via.placeholder.com/800x400?text=CLI+Demo+Here)

## 🚀 Deployment Guide

### Prerequisites
- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the system
```bash
python rag_qa.py --query "What is the mission status?"
```

> Note: You’ll need to integrate FAISS vector stores, LangChain chains, and load your preferred LLM checkpoint.

## 🛠 Tech Stack
- Python
- FAISS
- LangChain
- LLaMA / DeepSeek (via transformers or local inference)
- CLI interface

## 📄 License
This project is licensed under the MIT License.

---

## 👤 Author
**K L Mandara**  
[LinkedIn](https://www.linkedin.com/in/k-l-mandara) | [GitHub](https://github.com/KLMANDARA)
