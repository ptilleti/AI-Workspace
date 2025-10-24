# 🦙 Ollama Setup Guide - Run Free AI Models Locally!

Ollama lets you run powerful AI models on your own computer - completely free, no API keys needed!

## What is Ollama?

- **Free**: No API costs, no subscriptions
- **Private**: Your data never leaves your computer
- **Fast**: Runs directly on your hardware
- **Easy**: Simple commands to get started
- **Powerful**: Models like Llama 3.2, Mistral, Phi-3

## Step 1: Install Ollama

### Windows (You're here!)

1. **Download**: Visit [ollama.ai](https://ollama.ai/)
2. **Install**: Run the Windows installer
3. **Verify**: Open PowerShell and type:
   ```powershell
   ollama --version
   ```

That's it! Ollama will run as a background service automatically.

## Step 2: Download a Model

Ollama needs to download models before you can use them. Here are great starting models:

### Recommended Models

**Llama 3.2 (3B)** - Best for beginners! ⭐
- Size: ~2 GB
- Speed: Very fast on most computers
- Quality: Good for learning and general use
```powershell
ollama pull llama3.2
```

**Llama 3.2 (1B)** - Smallest, fastest
- Size: ~1.3 GB
- Speed: Extremely fast
- Quality: Good for simple tasks
```powershell
ollama pull llama3.2:1b
```

**Llama 3.1 (8B)** - More powerful
- Size: ~4.7 GB
- Speed: Moderate (needs good CPU/GPU)
- Quality: Better reasoning and knowledge
```powershell
ollama pull llama3.1
```

**Phi-3 (3.8B)** - Microsoft's model
- Size: ~2.3 GB
- Speed: Fast
- Quality: Great for coding and reasoning
```powershell
ollama pull phi3
```

### Check What You Have

See all downloaded models:
```powershell
ollama list
```

## Step 3: Test Ollama

Try chatting with the model directly:

```powershell
ollama run llama3.2
```

Type a question, press Enter. Type `/bye` to exit.

Example conversation:
```
>>> What is machine learning in one sentence?
Machine learning is...
>>> /bye
```

## Step 4: Configure Your Chatbot

Copy the example environment file:
```powershell
Copy-Item .env.example .env
```

Your `.env` file should look like this:
```bash
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
TEMPERATURE=0.7
```

That's it! No API key needed.

## Step 5: Run Your Chatbot

```powershell
python src/chatbot.py
```

Your chatbot now uses free local models! 🎉

## Understanding Ollama

### How It Works
1. **Ollama Server**: Runs in background (starts automatically on Windows)
2. **Models**: Downloaded once, stored locally
3. **API**: Your Python code talks to localhost:11434
4. **Processing**: All happens on your computer

### Model Sizes & Performance

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| llama3.2:1b | ~1.3 GB | ⚡⚡⚡ | ⭐⭐ | Testing, learning |
| llama3.2 (3b) | ~2 GB | ⚡⚡⚡ | ⭐⭐⭐ | **Recommended start** |
| phi3 | ~2.3 GB | ⚡⚡ | ⭐⭐⭐ | Code, reasoning |
| llama3.1 (8b) | ~4.7 GB | ⚡⚡ | ⭐⭐⭐⭐ | Better quality |
| mistral | ~4.1 GB | ⚡⚡ | ⭐⭐⭐⭐ | General purpose |

**Speed**: ⚡ = Fast on most PCs | ⚡⚡ = Needs decent CPU | ⚡⚡⚡ = Very fast

### Hardware Requirements

**Minimum** (llama3.2:1b):
- 8 GB RAM
- Any modern CPU
- No GPU needed

**Recommended** (llama3.2):
- 16 GB RAM
- Modern CPU (Intel i5/Ryzen 5 or better)
- Optional: GPU for faster inference

**Best** (llama3.1 8B+):
- 32 GB RAM
- Powerful CPU or GPU
- NVIDIA GPU: Significant speedup

### GPU Acceleration

Ollama automatically uses your GPU if available:
- **NVIDIA**: Works out of the box (CUDA)
- **AMD**: Some support (ROCm)
- **Apple Silicon**: Excellent (Metal)

Check if GPU is being used:
```powershell
ollama run llama3.2 --verbose
```

## Useful Commands

### Managing Models

```powershell
# List downloaded models
ollama list

# Download a model
ollama pull llama3.2

# Remove a model (free up space)
ollama rm llama3.2

# Update a model
ollama pull llama3.2

# Show model details
ollama show llama3.2
```

### Running Models

```powershell
# Interactive chat
ollama run llama3.2

# With custom system prompt
ollama run llama3.2 "You are a coding expert."

# Process a file
Get-Content prompt.txt | ollama run llama3.2
```

### Server Management

```powershell
# Check if server is running
Test-NetConnection localhost -Port 11434

# Restart Ollama (if needed)
# Just restart the Ollama app from Start menu
```

## Troubleshooting

### "Connection refused" or "Cannot connect to Ollama"

**Solution 1**: Check if Ollama is running
```powershell
Test-NetConnection localhost -Port 11434
```

**Solution 2**: Start Ollama
- Open Ollama from Start menu
- Or restart your computer (starts automatically)

**Solution 3**: Check firewall
- Allow Ollama through Windows Firewall

### "Model not found"

You need to download the model first:
```powershell
ollama pull llama3.2
```

### Slow Performance

Try a smaller model:
```powershell
ollama pull llama3.2:1b
```

Or close other applications to free up RAM.

### Out of Memory

Models are too large for your system. Try:
1. Use smaller model (llama3.2:1b)
2. Close other applications
3. Use quantized models (automatically used by Ollama)

## Comparing with OpenAI

| Feature | Ollama | OpenAI |
|---------|--------|--------|
| **Cost** | Free | ~$0.15-$10 per 1M tokens |
| **Privacy** | 100% local | Data sent to OpenAI |
| **Speed** | Depends on hardware | Usually fast |
| **Quality** | Good (varies by model) | Excellent |
| **Setup** | Install + download | Just API key |
| **Internet** | Not needed | Required |

### When to Use Ollama
✅ Learning and experimenting  
✅ Privacy-sensitive projects  
✅ No budget for API costs  
✅ Want to understand how LLMs work  
✅ Offline work needed  

### When to Use OpenAI
✅ Need best quality responses  
✅ Production applications  
✅ Don't want to manage infrastructure  
✅ Limited local hardware  

## Advanced Tips

### Custom Model Parameters

Edit your Python code to customize:

```python
response = client.chat.completions.create(
    model="llama3.2",
    messages=messages,
    temperature=0.7,      # Creativity
    max_tokens=2000,      # Response length
    top_p=0.9,           # Diversity
    frequency_penalty=0   # Repetition control
)
```

### Using Multiple Models

Switch models easily in `.env`:
```bash
OLLAMA_MODEL=llama3.2    # For speed
# OLLAMA_MODEL=llama3.1  # For quality
# OLLAMA_MODEL=phi3      # For coding
```

### Model Variants

Ollama offers different sizes:
```powershell
ollama pull llama3.2:1b    # 1 billion params (smallest)
ollama pull llama3.2       # 3 billion params (default)
ollama pull llama3.1:8b    # 8 billion params
ollama pull llama3.1:70b   # 70 billion params (huge!)
```

### Context Window

Different models have different context limits:
- Llama 3.2: 128K tokens (~96K words)
- Llama 3.1: 128K tokens
- Mistral: 32K tokens
- Phi-3: 128K tokens

This affects how much PDF content you can process at once.

## Learning Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Available Models](https://ollama.ai/library)
- [Model Cards](https://huggingface.co/models) - Detailed model info

## Next Steps

1. ✅ Install Ollama
2. ✅ Download llama3.2
3. ✅ Test with `ollama run llama3.2`
4. ✅ Configure `.env` with `LLM_PROVIDER=ollama`
5. ✅ Run your chatbot: `python src/chatbot.py`
6. 🚀 Start experimenting!

---

**Welcome to free local AI!** 🎉

You can now build AI applications without any costs. Perfect for learning, experimenting, and building privacy-focused projects.

Questions? Just ask! 🤖
