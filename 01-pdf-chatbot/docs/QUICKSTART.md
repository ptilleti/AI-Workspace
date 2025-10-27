# 🚀 Quick Start Guide

Get your PDF chatbot running in 5 minutes with **FREE local AI!**

For detailed Ollama information, see [OLLAMA_GUIDE.md](OLLAMA_GUIDE.md).

## Step 1: Choose Your Path

### 🆓 Path A: Ollama (Recommended - Free & Private!)

**Best for**: Learning, experimenting, privacy-focused projects

#### 1. Install Ollama
- Visit [ollama.ai](https://ollama.ai/) and download for Windows
- Install and it will run automatically

#### 2. Download a Model
Open PowerShell:
```powershell
ollama pull llama3.2
```
This downloads a 2GB model (one-time download).

#### 3. Install Python Dependencies
```powershell
pip install -r requirements.txt
```

#### 4. Configure Environment
```powershell
Copy-Item .env.example .env
```
Your `.env` is already set to use Ollama by default! No API key needed.

#### 5. Verify Setup
```powershell
.\check-ollama.ps1
```

✅ **Done!** Skip to "Add a PDF" below.

---

### 💳 Path B: OpenAI API (Paid, but Excellent Quality)

**Best for**: Production apps, need absolute best quality

#### 1. Get API Key
- Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Create new secret key (looks like `sk-...`)
- New accounts get $5 free credit

#### 2. Install Python Dependencies
```powershell
pip install -r requirements.txt
```

#### 3. Configure Environment
```powershell
Copy-Item .env.example .env
```
Edit `.env` and change:
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-actual-key-here
```

---

## Step 2: Add a PDF

Place any PDF file in the `data/` folder. For example:
- A book (from [Project Gutenberg](https://www.gutenberg.org/))
- A research paper from [arXiv](https://arxiv.org/)
- Technical documentation
- Any text-based PDF (not scanned images)

See `data/README.md` for more free PDF sources.

## Step 3: Run the Chatbot!

```powershell
python src/chatbot.py
```

That's it! Start asking questions about your PDF. 🎉

---

## 🎓 Learning Path

### Beginner: Interactive Tutorial
Open the Jupyter notebook for hands-on learning:

```powershell
jupyter notebook notebooks/tutorial.ipynb
```

This walks you through:
- How LLMs work (with Ollama!)
- PDF processing
- Building the chatbot step-by-step
- Testing different models

### Intermediate: Explore the Code

The project has 3 main modules:

1. **`src/pdf_processor.py`** - PDF text extraction
2. **`src/llm_client.py`** - LLM communication
3. **`src/chatbot.py`** - Main chatbot logic

Each file is heavily commented for learning.

### Advanced: Extend the Project

Ideas to try:
- Try different Ollama models (qwen2.5:7b, phi3, etc.)
- Add conversation memory
- Support multiple PDFs
- Build a web UI with Streamlit
- Implement RAG with vector databases (ChromaDB)

---

## 💰 Cost Comparison

### Using Ollama (Recommended):
- **Cost**: $0.00 forever! 🎉
- **Privacy**: 100% local, data never leaves your PC
- **Internet**: Not needed after model download
- **Quality**: Excellent (llama3.2, qwen2.5, phi3)
- **Speed**: Depends on your hardware (usually fast)

### Using OpenAI API:
- **Cost**: ~$0.001-0.005 per conversation (very cheap)
- **Quality**: Best available (GPT-4o)
- **Speed**: Usually very fast
- **Free tier**: $5 credit for new accounts

---

## 🐛 Troubleshooting

### Ollama Issues

**"Cannot connect to Ollama"**
```powershell
# Check if Ollama is running
Test-NetConnection localhost -Port 11434

# If not running, start Ollama from the Start menu
```

**"Model not found"**
```powershell
# Download the model first
ollama pull llama3.2
```

**Slow responses?**
```powershell
# Try a smaller/faster model
ollama pull llama3.2:1b
```

### General Issues

**"No module named 'openai'"**
```powershell
pip install -r requirements.txt
```

**"No PDF files found"**
Add a PDF to the `data/` folder

**Import errors in VS Code**
The red squiggles will disappear after installing packages:
```powershell
pip install -r requirements.txt
```

### OpenAI API Issues (if using OpenAI)

**"API key not found"**
Make sure `.env` has: `LLM_PROVIDER=openai` and `OPENAI_API_KEY=sk-...`

---

## 📚 Next Steps

1. ✅ Run the basic chatbot
2. 📓 Work through the Jupyter tutorial
3. 🔧 Modify the code and experiment
4. 🚀 Build something new!

**Questions?** Check the main README.md for more details.

Happy learning! 🎉
