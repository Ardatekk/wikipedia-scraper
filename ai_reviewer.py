import os
import google.generativeai as genai

# Fetch API key from GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("⚠️ GEMINI_API_KEY not found in environment variables!")
    exit(0)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Define target file for AI code review
scraper_filename = "main.py" 

try:
    with open(scraper_filename, "r", encoding="utf-8") as f:
        code_content = f.read()

    prompt = f"""
    You are a Senior Data Engineer and CI/CD Code Reviewer. 
    Review the following Python scraper code. Provide a concise, 3-bullet-point code review covering code quality, performance, and potential error handling:

    ```python
    {code_content}
    ```
    """

    print(" AI Code Reviewer analyzing target script...\n" + "="*40)
    response = model.generate_content(prompt)
    print(response.text)
    print("="*40)

except FileNotFoundError:
    print(f"❌ Target file '{scraper_filename}' was not found!")