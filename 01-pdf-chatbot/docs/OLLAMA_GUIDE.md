# 🦙 Ollama Guide - Free Local AI

Complete guide to using Ollama with your PDF chatbot.

## Quick Start (5 Minutes)

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai/)
2. **Download a model**:
   ```powershell
   ollama pull llama3.2
   ```
3. **Configure environment**:
   ```powershell
   Copy-Item .env.example .env
   # .env is already set to LLM_PROVIDER=ollama by default
   ```
4. **Run the chatbot**:
   ```powershell
   python src/chatbot.py
   ```

That's it! No API key needed. 🎉

---

## What is Ollama?

- **Free**: No API costs, no subscriptions
- **Private**: Your data never leaves your computer
- **Fast**: Runs directly on your hardware
- **Easy**: Simple commands to get started

---

## Recommended Models

| Model | Size | Speed | Quality | Command |
|-------|------|-------|---------|---------|
| **Llama 3.2** ⭐ | ~2 GB | ⚡⚡⚡ | ⭐⭐⭐ | `ollama pull llama3.2` |
| Llama 3.2 (1B) | ~1.3 GB | ⚡⚡⚡ | ⭐⭐ | `ollama pull llama3.2:1b` |
| Llama 3.1 (8B) | ~4.7 GB | ⚡⚡ | ⭐⭐⭐⭐ | `ollama pull llama3.1` |
| Phi-3 | ~2.3 GB | ⚡⚡ | ⭐⭐⭐ | `ollama pull phi3` |

**Speed**: ⚡ = Moderate | ⚡⚡ = Fast | ⚡⚡⚡ = Very Fast

### Switching Models

Edit `.env` and change the model:
```bash
OLLAMA_MODEL=llama3.2    # Default (recommended)
# OLLAMA_MODEL=llama3.1  # More powerful
# OLLAMA_MODEL=phi3      # Good for coding
```

Browse all models at: https://ollama.ai/library

---

## Essential Commands

```powershell
# Check installation
ollama --version

# Download a model
ollama pull llama3.2

# List downloaded models
ollama list

# Remove a model (free up space)
ollama rm llama3.2

# Chat with a model directly
ollama run llama3.2

# Check if Ollama server is running
Test-NetConnection localhost -Port 11434
```

---

## Hardware Requirements

**Minimum** (llama3.2:1b):
- 8 GB RAM
- Any modern CPU
- No GPU needed

**Recommended** (llama3.2):
- 16 GB RAM
- Modern CPU (Intel i5/Ryzen 5+)
- Optional GPU for faster inference

**Best** (llama3.1 8B+):
- 32 GB RAM
- Powerful CPU or NVIDIA GPU

Ollama automatically uses your GPU if available (NVIDIA, AMD, or Apple Silicon).

---

## Troubleshooting

### "Cannot connect to Ollama"

**Check if running:**
```powershell
Test-NetConnection localhost -Port 11434
```

**Start Ollama:**
- Open Ollama from Start menu
- Or restart your computer (auto-starts)

### "Model not found"

Download the model first:
```powershell
ollama pull llama3.2
```

### Slow Performance

Try a smaller model:
```powershell
ollama pull llama3.2:1b
```

Or close other applications to free up RAM.

---

## Ollama vs OpenAI

| Feature | Ollama | OpenAI |
|---------|--------|--------|
| **Cost** | Free | ~$0.001-0.005 per chat |
| **Privacy** | 100% local | Data sent to cloud |
| **Speed** | Depends on hardware | Usually fast |
| **Quality** | Good to Excellent | Excellent |
| **Internet** | Not needed | Required |

### When to Use Ollama
✅ Learning and experimenting  
✅ Privacy-sensitive projects  
✅ No budget for API costs  
✅ Want to understand how LLMs work  

### When to Use OpenAI
✅ Need best quality responses  
✅ Production applications  
✅ Limited local hardware  

---

## Advanced Tips

### Custom Parameters

Edit `src/llm_client.py` to customize:
```python
response = client.chat.completions.create(
    model="llama3.2",
    messages=messages,
    temperature=0.7,      # Creativity (0.0-1.0)
    max_tokens=2000,      # Response length
    top_p=0.9,           # Diversity
)
```

### Context Windows

- Llama 3.2: 128K tokens (~96K words)
- Llama 3.1: 128K tokens
- Phi-3: 128K tokens

This determines how much PDF content can be processed at once.

---

## Resources

- [Ollama Home](https://ollama.ai/)
- [Model Library](https://ollama.ai/library)
- [GitHub](https://github.com/ollama/ollama)

---

**You're ready to build with free local AI!** 🚀
