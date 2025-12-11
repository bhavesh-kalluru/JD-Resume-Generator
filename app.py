import streamlit as st
from openai import OpenAI
import textwrap

st.set_page_config(
    page_title="Resume Tailor – Job-Specific Optimization",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Resume Tailor – Job-Specific Optimization")
st.write(
    "Paste your **job description** and **base resume**, then generate a tailored version "
    "optimized for that specific role."
)

# Sidebar: API settings
st.sidebar.header("🔐 OpenAI API Settings")
api_key = st.sidebar.text_input(
    "OpenAI API key",
    type="password",
    help="Your key is only used locally in this app.",
)

default_model = "gpt-4o-mini"
model_name = st.sidebar.text_input(
    "Model name",
    value=default_model,
    help="For example: gpt-4o-mini, gpt-4o, gpt-4.1-mini",
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "This tool does not store your data. Everything runs in your local environment."
)


def build_prompt(job_description: str, base_resume: str) -> list:
    """Build the messages list for the chat completion call."""
    system_message = textwrap.dedent(
        """
        You are an expert resume writer and ATS optimization specialist.

        GOAL  
        Given:
        1) A target JOB DESCRIPTION  
        2) A BASE RESUME  

        Create a tailored resume that is highly aligned with the job description while
        staying honest and consistent with the candidate's background.

        IMPORTANT – DO NOT:
        - Change the candidate's full name, email, phone number, or location.
        - Change or fabricate LinkedIn, GitHub, or portfolio URLs.
        - Invent fake jobs, companies, projects, or degrees.
        - Modify existing employment dates or create fake ones.
        - Claim experience with tools/technologies that are clearly not present in the original resume.

        YOU MAY:
        - Rephrase and reorder bullet points for clarity and impact.
        - Emphasize skills and experience that best match the job description.
        - Group or slightly rename sections (Summary, Experience, Projects, Skills, Education, etc.).
        - Expand on responsibilities or impact that a typical professional in such roles could reasonably describe,
          as long as it is consistent with the original content.

        OUTPUT FORMAT:
        - Return the full tailored resume as clean text or Markdown.
        - Preserve a professional, concise tone.
        - Focus on strong, quantified impact where possible (e.g., percentages, counts, time saved).
        """
    ).strip()

    user_message = textwrap.dedent(
        f"""
        Here is the target job description:

        ---------------- JOB DESCRIPTION ----------------
        {job_description}
        -------------------------------------------------

        Here is the candidate's current base resume:

        ---------------- BASE RESUME ----------------
        {base_resume}
        -------------------------------------------------

        Please generate a tailored resume that follows all the rules above.
        """
    ).strip()

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]


def call_openai(api_key: str, model: str, messages: list, temperature: float = 0.3) -> str:
    """Call OpenAI's chat completion endpoint and return the response text."""
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content


# Main layout
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("1️⃣ Inputs")

    job_description = st.text_area(
        "Job Description",
        height=260,
        placeholder="Paste the full job description here...",
    )

    st.markdown("**Base Resume**")
    resume_source = st.radio(
        "How would you like to provide your resume?",
        ["Paste text", "Upload .txt file"],
        horizontal=True,
        label_visibility="collapsed",
    )

    resume_text = ""
    if resume_source == "Paste text":
        resume_text = st.text_area(
            "Base Resume (Text)",
            height=260,
            placeholder="Paste your current resume here (text only).",
            key="resume_text",
        )
    else:
        uploaded = st.file_uploader(
            "Upload a plain-text (.txt) version of your resume",
            type=["txt"],
            help="For best results, export your resume as .txt and upload it here.",
        )
        if uploaded is not None:
            resume_text = uploaded.read().decode("utf-8", errors="ignore")
            st.text_area(
                "Preview of Uploaded Resume",
                resume_text,
                height=260,
                key="resume_preview",
            )

    temperature = st.slider(
        "Creativity (temperature)",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Lower values = more conservative/precise, higher = more creative wording.",
    )

with col_right:
    st.subheader("2️⃣ Tailored Resume Output")
    output_placeholder = st.empty()

    if "tailored_resume" not in st.session_state:
        st.session_state["tailored_resume"] = ""

    if st.button("🚀 Generate Tailored Resume", use_container_width=True):
        if not api_key:
            st.error("Please enter your OpenAI API key in the sidebar.")
        elif not job_description.strip():
            st.error("Please paste the job description.")
        elif not resume_text.strip():
            st.error("Please provide your base resume (paste or upload a .txt file).")
        else:
            with st.spinner("Generating tailored resume with OpenAI..."):
                try:
                    messages = build_prompt(job_description, resume_text)
                    tailored = call_openai(
                        api_key,
                        model_name.strip() or default_model,
                        messages,
                        temperature=temperature,
                    )
                    st.session_state["tailored_resume"] = tailored
                    st.success("Tailored resume generated successfully!")
                except Exception as e:
                    st.error(f"Something went wrong while calling OpenAI: {e}")

    tailored_resume = st.session_state.get("tailored_resume", "")
    output_placeholder.text_area(
        "Tailored Resume",
        value=tailored_resume,
        height=500,
    )

    if tailored_resume:
        st.download_button(
            "💾 Download Tailored Resume (.txt)",
            data=tailored_resume.encode("utf-8"),
            file_name="tailored_resume.txt",
            mime="text/plain",
            use_container_width=True,
        )
        st.caption(
            "You can also copy-paste the text above into your preferred resume template or editor."
        )
