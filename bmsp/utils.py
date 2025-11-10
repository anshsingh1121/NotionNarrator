import os
import re
from pathlib import Path


def convert_images_to_html(content: str, file_index: int) -> str:
    """
    Convert markdown image syntax to HTML img tags.
    
    Args:
        content: Markdown content
        file_index: Index of the file (for proper image path)
    
    Returns:
        Content with images converted to HTML
    """
    # Pattern to match: ![alt text](images/X/image_Y.png)
    pattern = r'!\[(.*?)\]\((images/\d+/image_\d+\.png)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        return f'<img src="{image_path}" alt="{alt_text}" width="400">'
    
    return re.sub(pattern, replace_image, content)


def combine_md_files(input_folder: str = "bmsp", output_file: str = "bmsp/combined_notes.md") -> str:
    """
    Combine all numbered .md files in order and convert images to HTML.
    
    Args:
        input_folder: Folder containing the .md files
        output_file: Path for the combined output file
    
    Returns:
        Path to the combined markdown file
    """
    # Get all numbered md files (0.md through 17.md)
    md_files = []
    for i in range(18):  # 0 to 17
        file_path = Path(input_folder) / f"{i}.md"
        if file_path.exists():
            md_files.append((i, file_path))
    
    print(f"Found {len(md_files)} markdown files to combine")
    
    # Combine all files
    combined_content = []
    
    for index, file_path in md_files:
        print(f"Processing {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert images to HTML
        content = convert_images_to_html(content, index)
        
        # Add content with a separator
        combined_content.append(content)
        combined_content.append("\n\n---\n\n")  # Add separator between files
    
    # Join all content
    final_content = "".join(combined_content)
    
    # Write combined file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Combined markdown saved to: {output_path}")
    return str(output_path)


def markdown_to_pdf(md_file: str, output_pdf: str = "bmsp/combined_notes.pdf"):
    """
    Convert markdown file to PDF.
    
    Args:
        md_file: Path to the markdown file
        output_pdf: Path for the output PDF file
    """
    try:
        import markdown
        from xhtml2pdf import pisa
    except ImportError:
        print("\nRequired libraries not found. Installing...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'markdown', 'xhtml2pdf'])
        import markdown
        from xhtml2pdf import pisa
    
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'tables', 'fenced_code']
    )
    
    # Get the base path for images
    base_path = Path(md_file).parent.absolute()
    
    # Create full HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: Arial, Helvetica, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 30px;
                font-size: 24px;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 5px;
                margin-top: 25px;
                font-size: 20px;
            }}
            h3 {{
                color: #7f8c8d;
                margin-top: 20px;
                font-size: 16px;
            }}
            img {{
                max-width: 400px;
                height: auto;
                display: block;
                margin: 20px auto;
                border: 1px solid #ddd;
                padding: 5px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                font-size: 12px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                font-family: Courier New, monospace;
                font-size: 11px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 15px;
                overflow-x: auto;
                font-size: 11px;
            }}
            ul, ol {{
                margin: 15px 0;
                padding-left: 30px;
            }}
            li {{
                margin: 8px 0;
            }}
            hr {{
                border: none;
                border-top: 2px solid #bdc3c7;
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    print(f"Generating PDF: {output_pdf}")
    
    with open(output_pdf, "wb") as pdf_file:
        # Convert HTML to PDF
        pisa_status = pisa.CreatePDF(
            full_html,
            dest=pdf_file,
            path=str(base_path)  # Set base path for images
        )
    
    if pisa_status.err:
        print(f"Error creating PDF: {pisa_status.err}")
    else:
        print(f"PDF successfully created: {output_pdf}")


def main():
    """Main function to combine MD files and create PDF."""
    print("Starting MD files combination and PDF generation...")
    print("=" * 60)
    
    # Step 1: Combine all MD files
    combined_md = combine_md_files()
    
    print("\n" + "=" * 60)
    
    # Step 2: Convert to PDF
    markdown_to_pdf(combined_md)
    
    print("\n" + "=" * 60)
    print("Process completed successfully!")
    print(f"- Combined markdown: {combined_md}")
    print(f"- PDF output: bmsp/combined_notes.pdf")


if __name__ == "__main__":
    main()

