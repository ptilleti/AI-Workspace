# 🚀 Quick Start Guide

Get your PDF chatbot running in 5 minutes!

## Step 1: Install Python Dependencies

Open a terminal in this directory and run:

```bash
pip install -r requirements.txt
```

This installs:
- `openai` - To interact with OpenAI's GPT models
- `pypdf` - To extract text from PDFs
- `python-dotenv` - To manage API keys securely
- `jupyter` - For interactive learning notebooks

## Step 2: Set Up Your API Key

### Option A: Use OpenAI (Recommended for beginners)

1. **Get an API key**: Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Create API key**: Click "Create new secret key"
3. **Copy the key**: It looks like `sk-...`

### Option B: Use Local Models (Free, but more setup)

Install [Ollama](https://ollama.ai/) to run models locally (no API key needed!)

## Step 3: Configure Environment

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Step 4: Add a PDF

Place any PDF file in the `data/` folder. For example:
- A book (from Project Gutenberg)
- A research paper
- Technical documentation
- Any text-based PDF you want to chat with

See `data/README.md` for free PDF sources.

## Step 5: Run the Chatbot!

```bash
python src/chatbot.py
```

That's it! Start asking questions about your PDF.

---

## 🎓 Learning Path

### Beginner: Interactive Tutorial
Open the Jupyter notebook for hands-on learning:

```bash
jupyter notebook notebooks/tutorial.ipynb
```

This walks you through:
- How LLMs work
- PDF processing
- Building the chatbot step-by-step

### Intermediate: Explore the Code

The project has 3 main modules:

1. **`src/pdf_processor.py`** - PDF text extraction
2. **`src/llm_client.py`** - LLM communication
3. **`src/chatbot.py`** - Main chatbot logic

Each file is heavily commented for learning.

### Advanced: Extend the Project

Ideas to try:
- Add conversation memory
- Support multiple PDFs
- Build a web UI
- Implement RAG with vector databases
- Use local models (Ollama)

---

## 💰 Cost Considerations

Using OpenAI API:
- **gpt-4o-mini**: ~$0.15 per 1M input tokens (very cheap!)
- A typical chat might use 1,000-5,000 tokens
- **Estimate**: $0.001-0.005 per conversation

For free usage:
- Use Ollama with local models (no API costs)
- Use free tier credits from OpenAI ($5 free for new accounts)

---

## 🐛 Troubleshooting

### "No module named 'openai'"
Run: `pip install -r requirements.txt`

### "API key not found"
Make sure `.env` file exists and contains `OPENAI_API_KEY=...`

### "No PDF files found"
Add a PDF to the `data/` folder

### Import errors in VS Code
The packages need to be installed. The red squiggles will go away after running:
```bash
pip install -r requirements.txt
```

---

## 📚 Next Steps

1. ✅ Run the basic chatbot
2. 📓 Work through the Jupyter tutorial
3. 🔧 Modify the code and experiment
4. 🚀 Build something new!

**Questions?** Check the main README.md for more details.

Happy learning! 🎉
