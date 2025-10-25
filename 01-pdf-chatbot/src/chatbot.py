"""
PDF Chatbot - Main Application
A simple chatbot that answers questions about PDF documents using CAG.

Learning Notes:
- This ties together PDF processing and LLM interaction
- CAG = Context Augmented Generation: we give the LLM the full PDF as context
- The LLM uses the context to answer questions accurately
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from pdf_processor import PDFProcessor
from llm_client import LLMClient


class PDFChatbot:
    """A chatbot that answers questions about PDF documents."""
    
    def __init__(self, pdf_path: str):
        """
        Initialize the chatbot with a PDF.
        
        Args:
            pdf_path: Path to the PDF file
        """
        print("🚀 Initializing PDF Chatbot")
        print("=" * 60)
        
        # Load environment variables
        load_dotenv()
        
        # Process the PDF
        self.pdf_processor = PDFProcessor(pdf_path)
        self.pdf_content = self.pdf_processor.extract_text()
        
        print()
        
        # Initialize LLM client
        provider = os.getenv("LLM_PROVIDER", "openai")
        temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.llm = LLMClient(provider=provider, temperature=temperature)
        
        print("=" * 60)
        print("✅ Chatbot ready!")
        print()
    
    def ask(self, question: str) -> str:
        """
        Ask a question about the PDF.
        
        Args:
            question: User's question
            
        Returns:
            str: The chatbot's answer
        """
        system_prompt = (
            "You are a helpful assistant that answers questions based on the "
            "provided document. Use only information from the document to answer. "
            "If the answer is not in the document, say so clearly."
        )
        
        # This is where CAG happens! We pass the PDF content as context
        answer = self.llm.chat(
            user_message=question,
            system_message=system_prompt,
            context=self.pdf_content
        )
        
        return answer
    
    def interactive_mode(self):
        """Run an interactive chat session."""
        print("\n💬 Interactive Mode")
        print("-" * 60)
        print("Ask questions about the PDF (type 'quit' or 'exit' to stop)")
        print("-" * 60)
        print()
        
        while True:
            try:
                # Get user input
                question = input("You: ").strip()
                
                # Check for exit
                if question.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Goodbye!")
                    break
                
                # Skip empty inputs
                if not question:
                    continue
                
                # Get answer
                print()
                answer = self.ask(question)
                print(f"Bot: {answer}")
                print()
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print(" 📚 PDF CHATBOT - Learn AI by Building ".center(60))
    print("=" * 60 + "\n")
    
    # Find PDF files
    data_dir = Path(__file__).parent.parent / "data"
    pdf_files = list(data_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("❌ No PDF files found in the data/ folder")
        print("\n💡 To use this chatbot:")
        print("   1. Add a PDF file to the data/ folder")
        print("   2. Run this script again")
        print("\nExample: Place 'my_book.pdf' in the data/ folder")
        return
    
    # List available PDFs
    if len(pdf_files) > 1:
        print("📚 Available PDF files:")
        for i, pdf in enumerate(pdf_files, 1):
            print(f"   {i}. {pdf.name}")
        print()
        
        while True:
            try:
                choice = input(f"Select a PDF (1-{len(pdf_files)}): ").strip()
                index = int(choice) - 1
                if 0 <= index < len(pdf_files):
                    pdf_path = pdf_files[index]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(pdf_files)}")
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                return
        print()
    else:
        pdf_path = pdf_files[0]
    
    # Create and run chatbot
    try:
        chatbot = PDFChatbot(str(pdf_path))
        chatbot.interactive_mode()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Common issues:")
        print("   - Make sure .env file exists with OPENAI_API_KEY")
        print("   - Check that the PDF is not corrupted")
        print("   - Ensure you have internet connection for API calls")


if __name__ == "__main__":
    main()
