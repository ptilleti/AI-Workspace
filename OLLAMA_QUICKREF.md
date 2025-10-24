# 🚀 Ollama Quick Reference

## Essential Commands

### Getting Started
```powershell
# Check installation
ollama --version

# Pull a model (download)
ollama pull llama3.2

# List all downloaded models
ollama list

# Chat with a model
ollama run llama3.2
```

### Recommended Models for This Project

| Model | Command | Size | Best For |
|-------|---------|------|----------|
| **Llama 3.2** | `ollama pull llama3.2` | ~2 GB | ⭐ Recommended start |
| Llama 3.2 (1B) | `ollama pull llama3.2:1b` | ~1.3 GB | Fastest |
| Llama 3.1 (8B) | `ollama pull llama3.1` | ~4.7 GB | Better quality |
| Phi-3 | `ollama pull phi3` | ~2.3 GB | Great for code |

### Testing Your Setup

**Quick Test:**
```powershell
# 1. Check if Ollama is running
Test-NetConnection localhost -Port 11434

# 2. Run the verification script
.\check-ollama.ps1

# 3. Test the chatbot
python src/llm_client.py
```

### Configuration

**Your `.env` file should have:**
```bash
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
TEMPERATURE=0.7
```

### Switching Models

Edit `.env` and change `OLLAMA_MODEL`:
```bash
OLLAMA_MODEL=llama3.2    # Default
# OLLAMA_MODEL=llama3.1  # More powerful
# OLLAMA_MODEL=phi3      # Good for code
```

Or pull and use any model from: https://ollama.ai/library

### Troubleshooting

**Problem: "Cannot connect to Ollama"**
```powershell
# Solution: Make sure Ollama is running
# Open Ollama from Start menu, or restart your PC
```

**Problem: "Model not found"**
```powershell
# Solution: Download the model first
ollama pull llama3.2
```

**Problem: Slow responses**
```powershell
# Solution: Use a smaller model
ollama pull llama3.2:1b
```

### Cost Comparison

| Feature | Ollama | OpenAI |
|---------|--------|--------|
| Cost per chat | **$0.00** | ~$0.001-0.005 |
| Privacy | 100% local | Sent to cloud |
| Internet needed | No | Yes |
| Setup time | 5 minutes | 1 minute |

### Project Workflow

1. **One-time setup:**
   ```powershell
   # Install Ollama from ollama.ai
   ollama pull llama3.2
   pip install -r requirements.txt
   Copy-Item .env.example .env
   # Edit .env: LLM_PROVIDER=ollama
   ```

2. **Every time you code:**
   ```powershell
   # Ollama runs automatically (no need to start)
   python src/chatbot.py
   ```

### Learning Path

✅ **Week 1**: Get comfortable with Ollama
- Install and test different models
- Understand model sizes vs. performance
- Build the basic chatbot

✅ **Week 2**: Experiment
- Try different models for same questions
- Adjust temperature settings
- Process different PDFs

✅ **Week 3+**: Advanced
- Add RAG with vector databases
- Build more complex agents
- Deploy your application

### Links

- **Ollama Home**: https://ollama.ai/
- **Model Library**: https://ollama.ai/library
- **GitHub**: https://github.com/ollama/ollama
- **Setup Guide**: See OLLAMA_SETUP.md

---

**You're all set!** 🎉 Start building with free local AI!
