"""
PDF Processor Module
Extracts text content from PDF files for use in CAG (Context Augmented Generation).

Learning Notes:
- We use pypdf to read PDF files
- Text extraction can be imperfect (tables, images, etc.)
- For learning, we'll keep it simple and extract raw text
"""

from pathlib import Path
import pypdf


class PDFProcessor:
    """Handles PDF text extraction."""
    
    def __init__(self, pdf_path: str):
        """
        Initialize the PDF processor.
        
        Args:
            pdf_path: Path to the PDF file
        """
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        self.text_content = None
    
    def extract_text(self) -> str:
        """
        Extract all text from the PDF.
        
        Returns:
            str: Extracted text content
        """
        print(f"📄 Extracting text from: {self.pdf_path.name}")
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = pypdf.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                print(f"📖 Found {num_pages} pages")
                
                # Extract text from all pages
                text_parts = []
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    text_parts.append(text)
                    print(f"   Page {page_num}/{num_pages} extracted")
                
                self.text_content = "\n\n".join(text_parts)
                
                # Show statistics
                word_count = len(self.text_content.split())
                char_count = len(self.text_content)
                print(f"✅ Extraction complete!")
                print(f"   Words: {word_count:,}")
                print(f"   Characters: {char_count:,}")
                
                return self.text_content
                
        except Exception as e:
            raise Exception(f"Error extracting PDF text: {str(e)}")
    
    def get_preview(self, max_chars: int = 500) -> str:
        """
        Get a preview of the extracted text.
        
        Args:
            max_chars: Maximum characters to show
            
        Returns:
            str: Preview of text content
        """
        if self.text_content is None:
            raise ValueError("No text extracted yet. Call extract_text() first.")
        
        preview = self.text_content[:max_chars]
        if len(self.text_content) > max_chars:
            preview += "..."
        
        return preview


# Example usage (for testing)
if __name__ == "__main__":
    # This runs when you execute: python src/pdf_processor.py
    print("PDF Processor Test")
    print("-" * 50)
    
    # Try to find a PDF in the data folder
    from pathlib import Path
    data_dir = Path(__file__).parent.parent / "data"
    pdf_files = list(data_dir.glob("*.pdf"))
    
    if pdf_files:
        processor = PDFProcessor(pdf_files[0])
        text = processor.extract_text()
        print("\n📝 Preview:")
        print(processor.get_preview(300))
    else:
        print("❌ No PDF files found in data/ folder")
        print("💡 Add a PDF file to data/ to test extraction")
