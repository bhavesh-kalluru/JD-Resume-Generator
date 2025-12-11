# 📄 Resume Tailor – Streamlit App

A Streamlit web application that helps you generate a **job-specific tailored resume** using the OpenAI API.

You paste:
- A **job description**
- Your **base resume**

The app then generates a tailored resume aligned with that job, while keeping your real experience honest and consistent.

---

## 👤 About the Developer

I am a software developer with **5 years of experience**, currently **looking for a full-time role in the USA**.

---

## ✅ Prerequisites

- Python 3.9+ (3.10/3.11/3.12 also fine)  
- `pip` (Python package manager)  
- An **OpenAI API key**  
  - You can get one from your OpenAI account dashboard.

---

## 🚀 Getting Started (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/resume_tailor_streamlit_app.git
cd resume_tailor_streamlit_app
🔁 Replace <your-username> with your actual GitHub username.

2️⃣ (Optional) Create and Activate a Virtual Environment
macOS / Linux:

bash
Copy code
python -m venv .venv
source .venv/bin/activate
Windows (Command Prompt):

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set Your OpenAI API Key (Optional but Recommended)
You can either set it as an environment variable or just paste it into the app sidebar.

macOS / Linux (temporary for current session):

bash
Copy code
export OPENAI_API_KEY="your-openai-api-key-here"
Windows (PowerShell):

powershell
Copy code
$env:OPENAI_API_KEY="your-openai-api-key-here"
5️⃣ Run the Streamlit App
bash
Copy code
streamlit run app.py
You should see output like:

text
Copy code
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
Open the Local URL in your browser.

🖥️ Using the App
Enter API Key
In the left sidebar, paste your OpenAI API key (if not set via environment variable).

Paste Job Description

In the “Job Description” text area, paste the full job description.

Provide Base Resume
Choose either:

Paste text → paste your resume directly, or

Upload .txt file → upload a plain-text version of your resume.

Adjust Creativity (temperature)

Lower values (e.g. 0.2–0.3) → more focused and strict

Higher values (e.g. 0.7–0.9) → more creative wording

Click “🚀 Generate Tailored Resume”

The app will call OpenAI.

The tailored resume will appear in the right panel.

Download

Click “💾 Download Tailored Resume (.txt)” to save the result.

⚙️ Git Commands Cheat Sheet
Here are the main git commands used to track and push this project to GitHub.

1️⃣ Initialize Git (first time only)
bash
Copy code
cd /path/to/resume_tailor_streamlit_app
git init
2️⃣ Add Files and Commit
bash
Copy code
git add .
git commit -m "Initial commit: Resume Tailor Streamlit app"
If git asks for your identity, configure it:

bash
Copy code
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
Then run the git commit command again.

3️⃣ Connect to GitHub Remote
Create an empty repo on GitHub (without README) and then:

bash
Copy code
git branch -M main
git remote add origin https://github.com/<your-username>/resume_tailor_streamlit_app.git
Replace <your-username> with your actual username.

4️⃣ Push Code to GitHub
bash
Copy code
git push -u origin main
Now your app.py, requirements.txt, and README.md will be visible on GitHub.

5️⃣ After Making Changes (Update Repo)
Whenever you update the code:

bash
Copy code
git add .
git commit -m "Describe what changed"
git push
🧪 Testing the Setup
To quickly verify everything works:

bash
Copy code
# From project root
pip install -r requirements.txt
streamlit run app.py
If the app opens in the browser and lets you:

Paste a job description

Paste/upload your base resume

Generate and download a tailored resume

…then everything is working correctly.

📫 Contact
If you’re interested in:

Collaborating on AI + web app projects

Hiring a developer with 5 years of experience who is actively looking for full-time roles in the USA

You can reach out via:

GitHub: https://github.com/<your-username>

(Add LinkedIn or email here if you want)
