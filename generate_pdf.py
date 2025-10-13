#!/usr/bin/env python3
"""
Generate PDF from DEPLOYMENT_STATUS.md using markdown2pdf
"""
import subprocess
import sys

def install_package(package):
    """Install a Python package using pip"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def generate_pdf():
    """Generate PDF from markdown file"""
    try:
        # Try importing markdown2pdf
        try:
            from markdown2pdf import markdown2pdf
            print("Using markdown2pdf...")
            markdown2pdf("DEPLOYMENT_STATUS.md", "DEPLOYMENT_STATUS.pdf")
            print("✅ PDF generated successfully: DEPLOYMENT_STATUS.pdf")
        except ImportError:
            print("markdown2pdf not found, installing...")
            install_package("markdown2pdf")
            from markdown2pdf import markdown2pdf
            markdown2pdf("DEPLOYMENT_STATUS.md", "DEPLOYMENT_STATUS.pdf")
            print("✅ PDF generated successfully: DEPLOYMENT_STATUS.pdf")
    except Exception as e:
        print(f"markdown2pdf failed: {e}")
        print("\nTrying alternative method with pdfkit...")
        try:
            import pdfkit
            import markdown
            
            # Read markdown file
            with open("DEPLOYMENT_STATUS.md", "r") as f:
                md_content = f.read()
            
            # Convert markdown to HTML
            html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
            
            # Add CSS styling
            styled_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        line-height: 1.6;
                        max-width: 900px;
                        margin: 40px auto;
                        padding: 20px;
                    }}
                    h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                    h2 {{ color: #34495e; margin-top: 30px; }}
                    h3 {{ color: #7f8c8d; }}
                    code {{
                        background-color: #f4f4f4;
                        padding: 2px 6px;
                        border-radius: 3px;
                        font-family: 'Courier New', monospace;
                    }}
                    pre {{
                        background-color: #f4f4f4;
                        padding: 15px;
                        border-radius: 5px;
                        overflow-x: auto;
                    }}
                    pre code {{
                        background-color: transparent;
                        padding: 0;
                    }}
                    ul {{ margin-left: 20px; }}
                    li {{ margin: 5px 0; }}
                    a {{ color: #3498db; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            # Save HTML temporarily
            with open("temp_deployment.html", "w") as f:
                f.write(styled_html)
            
            # Convert HTML to PDF
            pdfkit.from_file("temp_deployment.html", "DEPLOYMENT_STATUS.pdf")
            
            # Clean up
            import os
            os.remove("temp_deployment.html")
            
            print("✅ PDF generated successfully: DEPLOYMENT_STATUS.pdf")
            
        except ImportError:
            print("pdfkit not found, installing required packages...")
            install_package("pdfkit")
            install_package("markdown")
            print("Please run this script again after installation.")
        except Exception as e2:
            print(f"pdfkit also failed: {e2}")
            print("\nPlease install wkhtmltopdf system package:")
            print("sudo apt-get install wkhtmltopdf")

if __name__ == "__main__":
    generate_pdf()
