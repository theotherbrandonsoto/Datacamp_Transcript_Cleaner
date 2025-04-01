import pyperclip
import re

def process_text():
    # Get text from clipboard
    text = pyperclip.paste()
    
    # Remove lines containing timestamps (entire line with patterns like 00:00 - 00:08)
    text = re.sub(r'^.*\d{2}:\d{2}\s*-\s*\d{2}:\d{2}.*\n', '', text, flags=re.MULTILINE)
    
    # Add extra blank line between paragraphs
    # First, normalize all multiple blank lines to single blank lines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Then add one more blank line between numbered sections
    text = re.sub(r'\n\n(\d+\.)', '\n\n\n\\1', text)
    
    # Copy processed text back to clipboard
    pyperclip.copy(text)
    print("Text has been processed and copied to clipboard!")
    print("\nProcessed text:")
    print("-" * 50)
    print(text)
    print("-" * 50)

if __name__ == "__main__":
    process_text()