# 🤖 AI Learning Workspace# AI Learning Journey - PDF Chatbot



Welcome to my AI development learning journey! This repository contains multiple small projects as I learn to build AI applications, work with LLMs, and explore AI agent concepts.## Project Overview

A simple chatbot that can answer questions about a PDF document using Context Augmented Generation (CAG).

## 📚 Projects

## Learning Objectives

### [01-pdf-chatbot](./01-pdf-chatbot/) - PDF Question Answering Chatbot- Understand how to interact with LLMs

**Status**: ✅ Complete  - Learn PDF text extraction

**Tech**: Python, Ollama/OpenAI, PyPDF  - Implement context-based question answering

**Concepts**: CAG (Context Augmented Generation), LLM interaction, Prompt engineering- Build foundational AI agent concepts



A chatbot that answers questions about PDF documents using local AI models (Ollama) or OpenAI API. Perfect introduction to:## Project Structure

- Working with LLMs```

- PDF text extractionai-workspace/

- Context-based question answering├── README.md              # This file

- Free local AI with Ollama├── requirements.txt       # Python dependencies

├── .env.example          # Example environment variables

**Quick Start**:├── src/

```powershell│   ├── chatbot.py        # Main chatbot logic

cd 01-pdf-chatbot│   ├── pdf_processor.py  # PDF text extraction

pip install -r requirements.txt│   └── llm_client.py     # LLM interaction wrapper

# Follow docs/QUICKSTART.md├── data/

```│   └── sample.pdf        # Place your PDF here

└── notebooks/

---    └── tutorial.ipynb    # Interactive learning notebook

```

### 02-[Your Next Project]

Coming soon...## Setup Instructions



---**🆓 Want FREE local AI?** See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for complete Ollama setup!



## 🛠️ Development Environment### Quick Start with Ollama (Recommended for Learning)



### Prerequisites1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/)

- Python 3.8+2. **Download a model**: 

- [Ollama](https://ollama.ai/) (for free local AI)   ```powershell

- Git   ollama pull llama3.2

   ```

### Project Organization3. **Install Python dependencies**:

   ```powershell

Each project is self-contained:   pip install -r requirements.txt

```   ```

project-name/4. **Configure environment**:

├── README.md           # Project overview & instructions   ```powershell

├── requirements.txt    # Python dependencies   Copy-Item .env.example .env

├── .env.example        # Environment variables template   ```

├── src/               # Source code   Make sure `.env` has: `LLM_PROVIDER=ollama`

│   └── __init__.py    # Python package marker5. **Verify setup**:

├── data/              # Project data   ```powershell

├── notebooks/         # Jupyter notebooks (if any)   .\check-ollama.ps1

└── docs/              # Additional documentation   ```

```6. **Add a PDF** to the `data/` folder

7. **Run the chatbot**:

### Working with Projects   ```powershell

   python src/chatbot.py

```powershell   ```

# Navigate to a project

cd 01-pdf-chatbot### Alternative: OpenAI API Setup



# Create virtual environment (recommended)If you prefer using OpenAI (requires API key and costs money):

python -m venv venv

.\venv\Scripts\Activate.ps11. **Install Python Dependencies**

   ```powershell

# Install dependencies   pip install -r requirements.txt

pip install -r requirements.txt   ```



# Run the project2. **Get API Key**: Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

python src/main_script.py

```3. **Configure Environment Variables**

   ```powershell

## 🎯 Learning Path   Copy-Item .env.example .env

   ```

1. **PDF Chatbot (CAG)** ← You are here   Edit `.env` and set:

   - Learn LLM basics   ```

   - Understand context windows   LLM_PROVIDER=openai

   - Practice prompt engineering   OPENAI_API_KEY=your_key_here

   ```

2. **RAG Chatbot** (Planned)

   - Vector databases (ChromaDB)4. **Add Your PDF** to the `data/` folder

   - Embeddings

   - Retrieval Augmented Generation5. **Run the Chatbot**

   ```powershell

3. **Multi-Tool AI Agent** (Planned)   python src/chatbot.py

   - Function calling   ```

   - Tool integration

   - Agent frameworks (LangChain)## Concepts Explained



4. **Autonomous Agent** (Planned)### What is CAG (Context Augmented Generation)?

   - Planning and reasoning- We extract all text from the PDF

   - Multi-step workflows- When a user asks a question, we send the PDF text + question to the LLM

   - Agent memory systems- The LLM answers based on the provided context

- Simpler than RAG, works great for smaller documents

## 📖 General Resources

### Why Python?

### AI/LLM Learning- Rich ecosystem (langchain, openai, pypdf, etc.)

- [Ollama Documentation](https://github.com/ollama/ollama)- Easy to learn and prototype

- [OpenAI API Docs](https://platform.openai.com/docs)- Industry standard for AI/ML

- [LangChain Documentation](https://python.langchain.com/)

- [Prompt Engineering Guide](https://www.promptingguide.ai/)### Do I Need Docker?

- **Not for starting!** Docker is for deployment/production

### Python for AI- We'll run everything locally first

- [Real Python](https://realpython.com/)- Docker comes later when you want to containerize your app

- [Python Type Hints](https://docs.python.org/3/library/typing.html)

- [Poetry for Dependency Management](https://python-poetry.org/)## Next Steps

1. Start with the Jupyter notebook tutorial

### Communities2. Run the basic chatbot

- r/LocalLLaMA - Local models3. Experiment with different questions

- r/LangChain - LangChain framework4. Learn about improvements (RAG, vector databases, etc.)

- r/MachineLearning - ML/AI general

## 🔧 Shared Tools & Utilities

Common utilities used across projects can be found in the `shared/` folder (when needed).

## 📝 Notes & Learnings

### Key Insights
- **Start local**: Ollama is perfect for learning without API costs
- **Context windows matter**: Understand token limits for each model
- **Prompt engineering is crucial**: Small changes = big differences
- **Iterate fast**: Local models let you experiment freely

### Model Recommendations
- **llama3.2** (3B): Great all-rounder, fast, 128K context
- **qwen2.5:7b**: Better for technical content
- **phi3:medium**: Best quality for Q&A tasks

## 🤝 Contributing

This is a personal learning repo, but if you find these projects helpful:
- ⭐ Star the repo
- 🐛 Report issues
- 💡 Suggest improvements
- 🔗 Share with others learning AI

## 📄 License

This repository is for educational purposes. Individual projects may have their own licenses.

---

**Happy Learning!** 🚀

*Last Updated: October 2025*
