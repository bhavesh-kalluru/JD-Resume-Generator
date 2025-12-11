
# Resume Tailor – Streamlit App

This is a simple Streamlit app that helps you generate a **job-specific tailored resume** using the OpenAI API.

## Features

- Paste a **job description** and your **base resume**
- Uses OpenAI to rewrite and optimize your resume for that specific job
- Respects important constraints:
  - Does **not** invent fake jobs, companies, or degrees
  - Does **not** change your name/contact info
- Download the tailored resume as a `.txt` file

## How to run

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key (recommended) as an environment variable:

   ```bash
   export OPENAI_API_KEY="your-key-here"  # On Windows: setx OPENAI_API_KEY "your-key-here"
   ```

   > You can also paste the key directly into the app sidebar.

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## Notes

- The app expects you to paste plain-text resumes or upload a `.txt` version.
- You can adapt the prompt in `app.py` if you want stricter or looser behavior.
