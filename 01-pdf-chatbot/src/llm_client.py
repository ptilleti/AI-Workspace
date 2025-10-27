"""
LLM Client Module
Handles communication with Large Language Models (OpenAI, Ollama, etc.)

Learning Notes:
- LLMs work by predicting the next token (word/character)
- We send a "system prompt" (instructions) and "user prompt" (question)
- Temperature controls randomness (0 = deterministic, 1 = creative)
- Context window = max tokens the model can process at once
"""

import os
from typing import Optional
from openai import OpenAI


class LLMClient:
    """Client for interacting with LLMs."""
    
    def __init__(
        self,
        provider: str = "openai",
        model: Optional[str] = None,
        temperature: float = 0.7,
        api_key: Optional[str] = None
    ):
        """
        Initialize the LLM client.
        
        Args:
            provider: LLM provider ('openai' or 'ollama')
            model: Model name (e.g., 'gpt-4o-mini' or 'llama2')
            temperature: Response randomness (0.0-1.0)
            api_key: API key for the provider (if needed)
        """
        self.provider = provider
        self.temperature = temperature
        
        if provider == "openai":
            self.api_key = api_key or os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError(
                    "OpenAI API key not found. "
                    "Set OPENAI_API_KEY in .env or pass api_key parameter"
                )
            self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            self.client = OpenAI(api_key=self.api_key)
            
        elif provider == "ollama":
            # Ollama uses OpenAI-compatible API (no API key needed!)
            self.model = model or os.getenv("OLLAMA_MODEL", "llama3.2")
            # Point to local Ollama server
            self.client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"  # Ollama doesn't need a real key, but API requires something
            )
            print(f"💡 Using local Ollama server at http://localhost:11434")
            print(f"   Make sure Ollama is running: ollama serve")
            
        else:
            raise ValueError(f"Unknown provider: {provider}")
        
        print(f"🤖 Initialized {provider} client with model: {self.model}")
    
    def chat(
        self,
        user_message: str,
        system_message: str = "You are a helpful assistant.",
        context: Optional[str] = None
    ) -> str:
        """
        Send a chat message to the LLM.
        
        Args:
            user_message: The user's question/prompt
            system_message: Instructions for the LLM behavior
            context: Additional context (e.g., PDF content)
            
        Returns:
            str: The LLM's response
        """
        # Build messages with context (this is the CAG part!)
        messages = [
            {"role": "system", "content": system_message}
        ]
        
        # Add context in the USER message for better clarity
        if context:
            # Truncate context if too large (rough limit: 7500 tokens = ~30000 chars)
            # This leaves room for the system message, question, and response
            max_context_chars = 30000
            truncated = False
            
            if len(context) > max_context_chars:
                context = context[:max_context_chars]
                truncated = True
            
            print(f"📝 Context provided: {len(context)} characters" + 
                  (" (truncated)" if truncated else ""))
            
            # Put context BEFORE the question in the user message
            full_user_message = f"""Here is the document content to reference:

---BEGIN DOCUMENT---
{context}
---END DOCUMENT---

Based on the document above, please answer this question:
{user_message}"""
            messages.append({"role": "user", "content": full_user_message})
        else:
            print("⚠️  No context provided!")
            messages.append({"role": "user", "content": user_message})
        
        # Call the LLM
        try:
            print("🤔 Thinking...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=2000  # Increased for better responses
            )
            
            answer = response.choices[0].message.content
            
            # Show token usage (helpful for learning about costs)
            # Note: Ollama may not always return usage stats
            if hasattr(response, 'usage') and response.usage:
                usage = response.usage
                print(f"📊 Tokens used: {usage.total_tokens} "
                      f"(prompt: {usage.prompt_tokens}, "
                      f"completion: {usage.completion_tokens})")
            
            return answer
            
        except Exception as e:
            raise Exception(f"Error calling LLM: {str(e)}")
    
    def estimate_tokens(self, text: str) -> int:
        """
        Rough estimate of tokens in text.
        Rule of thumb: 1 token ≈ 4 characters or 0.75 words
        
        Args:
            text: Text to estimate
            
        Returns:
            int: Estimated token count
        """
        # Simple estimation (not exact, but good enough)
        return len(text) // 4


# Example usage (for testing)
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("LLM Client Test")
    print("-" * 50)
    
    # Get provider from environment or default to ollama
    provider = os.getenv("LLM_PROVIDER", "ollama")
    
    try:
        client = LLMClient(provider=provider)
        
        # Simple test
        response = client.chat(
            user_message="What is AI in one sentence?",
            system_message="You are a teacher explaining concepts simply."
        )
        
        print("\n💬 Response:")
        print(response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if provider == "openai":
            print("\n💡 Make sure you've:")
            print("   1. Copied .env.example to .env")
            print("   2. Added your OPENAI_API_KEY to .env")
        elif provider == "ollama":
            print("\n💡 Make sure you've:")
            print("   1. Installed Ollama from https://ollama.ai/")
            print("   2. Started Ollama: ollama serve")
            print("   3. Pulled a model: ollama pull llama3.2")
