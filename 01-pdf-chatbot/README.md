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
01-pdf-chatbot/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── check-ollama.ps1      # Ollama verification script
├── src/
│   ├── __init__.py       # Python package marker
│   ├── chatbot.py        # Main chatbot logic
│   ├── pdf_processor.py  # PDF text extraction
│   └── llm_client.py     # LLM interaction wrapper
├── data/
│   └── README.md         # Place your PDF here
├── notebooks/
│   └── tutorial.ipynb    # Interactive learning notebook
└── docs/
    ├── QUICKSTART.md     # 5-minute setup guide
    ├── OLLAMA_GUIDE.md   # Complete Ollama guide
    └── CONCEPTS.md       # AI concepts explained
```

## Setup Instructions

**🆓 Want FREE local AI?** See [docs/OLLAMA_GUIDE.md](docs/OLLAMA_GUIDE.md) for complete setup!

**⚡ Quick setup?** See [docs/QUICKSTART.md](docs/QUICKSTART.md) for 5-minute guide!

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
- **Note**: The chatbot automatically truncates PDFs larger than ~30,000 characters to fit within the model's context window

### Technical Implementation
- Context is included in the **user message** with clear delimiters (`---BEGIN DOCUMENT---`)
- This ensures the LLM properly recognizes and uses the document content
- Maximum response length: 2,000 tokens for detailed answers

### Why Python?
- Rich ecosystem (langchain, openai, pypdf, etc.)
- Easy to learn and prototype
- Industry standard for AI/ML

### Do I Need Docker?
- **Not for starting!** Docker is for deployment/production
- We'll run everything locally first
- Docker comes later when you want to containerize your app

## Next Steps
1. Start with the Jupyter notebook tutorial (`notebooks/tutorial.ipynb`)
2. Run the basic chatbot with `python src/chatbot.py`
3. Experiment with different questions
4. Try different Ollama models (see `docs/OLLAMA_GUIDE.md`)
5. Learn about improvements (RAG, vector databases, etc.)

**Note**: The tutorial notebook contains simplified example code for learning. The actual implementation in `src/` uses the optimized approach described above.
