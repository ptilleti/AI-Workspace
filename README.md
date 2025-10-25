# 🤖 AI Learning Workspace

Welcome to my AI development learning journey! This repository contains multiple small projects as I learn to build AI applications, work with LLMs, and explore AI agent concepts.

## 📚 Projects

### [01-pdf-chatbot](./01-pdf-chatbot/) - PDF Question Answering Chatbot
**Status**: ✅ Complete  
**Tech**: Python, Ollama/OpenAI, PyPDF  
**Concepts**: CAG (Context Augmented Generation), LLM interaction, Prompt engineering

A chatbot that answers questions about PDF documents using local AI models (Ollama) or OpenAI API. Perfect first project to learn:
- Working with LLMs
- PDF text extraction
- Context-based question answering
- Free local AI with Ollama

**Quick Start**:
```powershell
cd 01-pdf-chatbot
pip install -r requirements.txt
# Follow docs/QUICKSTART.md
```

---

### 02-[Your Next Project]
Coming soon...

---

## 🛠️ Development Environment

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) (for free local AI)
- Git

### Project Organization

Each project is self-contained:
```
project-name/
├── README.md           # Project overview & instructions
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── src/               # Source code
│   └── __init__.py    # Python package marker
├── data/              # Project data
├── notebooks/         # Jupyter notebooks (if any)
└── docs/              # Additional documentation
```

### Working with Projects

```powershell
# Navigate to a project
cd 01-pdf-chatbot

# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the project
python src/chatbot.py
```

## 🎯 Learning Path

1. **PDF Chatbot (CAG)** ← You are here
   - Learn LLM basics
   - Understand context windows
   - Practice prompt engineering

2. **RAG Chatbot** (Planned)
   - Vector databases (ChromaDB)
   - Embeddings
   - Retrieval Augmented Generation

3. **Multi-Tool AI Agent** (Planned)
   - Function calling
   - Tool integration
   - Agent frameworks (LangChain)

4. **Autonomous Agent** (Planned)
   - Planning and reasoning
   - Multi-step workflows
   - Agent memory systems

## 📖 General Resources

### AI/LLM Learning
- [Ollama Documentation](https://github.com/ollama/ollama)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Python for AI
- [Real Python](https://realpython.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Poetry for Dependency Management](https://python-poetry.org/)

### Communities
- r/LocalLLaMA - Local models
- r/LangChain - LangChain framework
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
