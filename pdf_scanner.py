import PyPDF2

def read_pdf_with_pypdf2(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        # Initialize a variable to keep all texts
        full_text = ""
        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the page
            page_text = pdf_reader.pages[page_num].extract_text()
            full_text += page_text + "\n" # Add the text of the page to the full_text
        return full_text

# Example usage
pdf_file_path = "/content/drive/MyDrive/Colab Notebooks/122014018_charansai.pdf"
print(read_pdf_with_pypdf2(pdf_file_path))
