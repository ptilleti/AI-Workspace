# AI Learning Journey - PDF Chatbot

## Project Overview
A simple chatbot that can answer questions about a PDF document using Context Augmented Generation (CAG).

## Learning Objectives
- Understand how to interact with LLMs
- Learn PDF text extraction
- Implement context-based question answering
- Build foundational AI agent concepts

## Project Structure
```
ai-workspace/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── src/
│   ├── chatbot.py        # Main chatbot logic
│   ├── pdf_processor.py  # PDF text extraction
│   └── llm_client.py     # LLM interaction wrapper
├── data/
│   └── sample.pdf        # Place your PDF here
└── notebooks/
    └── tutorial.ipynb    # Interactive learning notebook
```

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

### 3. Add Your PDF
Place your PDF file in the `data/` folder.

### 4. Run the Chatbot
```bash
python src/chatbot.py
```

## Concepts Explained

### What is CAG (Context Augmented Generation)?
- We extract all text from the PDF
- When a user asks a question, we send the PDF text + question to the LLM
- The LLM answers based on the provided context
- Simpler than RAG, works great for smaller documents

### Why Python?
- Rich ecosystem (langchain, openai, pypdf, etc.)
- Easy to learn and prototype
- Industry standard for AI/ML

### Do I Need Docker?
- **Not for starting!** Docker is for deployment/production
- We'll run everything locally first
- Docker comes later when you want to containerize your app

## Next Steps
1. Start with the Jupyter notebook tutorial
2. Run the basic chatbot
3. Experiment with different questions
4. Learn about improvements (RAG, vector databases, etc.)
