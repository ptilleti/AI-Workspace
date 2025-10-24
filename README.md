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

**🆓 Want FREE local AI?** See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for complete Ollama setup!

### Quick Start with Ollama (Recommended for Learning)

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/)
2. **Download a model**: 
   ```powershell
   ollama pull llama3.2
   ```
3. **Install Python dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
4. **Configure environment**:
   ```powershell
   Copy-Item .env.example .env
   ```
   Make sure `.env` has: `LLM_PROVIDER=ollama`
5. **Verify setup**:
   ```powershell
   .\check-ollama.ps1
   ```
6. **Add a PDF** to the `data/` folder
7. **Run the chatbot**:
   ```powershell
   python src/chatbot.py
   ```

### Alternative: OpenAI API Setup

If you prefer using OpenAI (requires API key and costs money):

1. **Install Python Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Get API Key**: Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

3. **Configure Environment Variables**
   ```powershell
   Copy-Item .env.example .env
   ```
   Edit `.env` and set:
   ```
   LLM_PROVIDER=openai
   OPENAI_API_KEY=your_key_here
   ```

4. **Add Your PDF** to the `data/` folder

5. **Run the Chatbot**
   ```powershell
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
