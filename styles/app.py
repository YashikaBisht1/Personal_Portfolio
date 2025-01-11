import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "../assets" / "cv.pdf"
profile_pic = current_dir / "../assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yashika Bisht"
PAGE_ICON = ":wave:"
NAME = "Yashika Bisht"
DESCRIPTION = """
IT undergraduate with hands-on experience in software engineering, data analysis, and machine learning.
"""
EMAIL = "bishty2005@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/YashikaBisht1",
    "LinkedIn": "https://linkedin.com/in/yashika-bisht-20050a24a",
    "Leetcode": "https://leetcode.com/bishty2005/",
    "Medium": "https://medium.com/@bishty2005"
}
PROJECTS = {
    "Credit Card Fraud Detection": {
        "description": "This research-based project involved building a machine learning model and implementing it on Streamlit to provide an interactive interface for users. The project uses various algorithms like KNN, Logistic Regression, and GRU for detecting fraud in credit card transactions. It also addresses class imbalance using SMOTE-ENN.",
        "link": "https://github.com/YashikaBisht1/Credit-Card-Fraud-detection.git"
    },
    "Intelligent Code Debugger and Summarizer": {
        "description": "Developed an AI-powered Python Code Debugger and Summarizer using Streamlit, CodeT5, and Google GenAI to detect syntax errors, identify unused variables, generate bug fixes, and summarize code functionality.",
        "link": "https://github.com/YashikaBisht1/Intelligent-code-debugger-and-Summariser.git"
    },
    "Personalized Chatbot (Work in Progress)": {
        "description": "Building a personalized chatbot leveraging Streamlit and LLMs to enhance user interactions and query handling.",
        "link": "#"
    }
    "GenAi cold email generator":{
        "description":Leveraged Llama3.1, LangChain, and ChromaDB for personalized email generation. Enhanced client outreach for software/AI services.",
        "link": "https://github.com/YashikaBisht1/project-genai-cold-email-generator"
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD PDF & PROFILE PIC ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="\U0001F4C4 Download Resume",
        data=PDFbyte,
        file_name=Path(resume_file).name,
        mime="application/octet-stream",
    )

    st.write("\U0001F4E7", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
    - \u2714 Virtual Software Engineering Internships at JPMorgan and Goldman Sachs.
    - \u2714 Data Analytics Certified by Microsoft and LinkedIn.
    - \u2714 Strong skills in Python, Machine Learning, and Git.
    - \u2714 Experience with web development using HTML, CSS, JavaScript, PHP.
    - \u2714 Solved 350+ coding problems on LeetCode.
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
    - \U0001F469‍\U0001F4BB Programming: Python (Intermediate), C++, C, JavaScript (Novice), Java (Novice).
    - \U0001F4D3 Technologies: Git, DialogFlow, Machine Learning, Prompt Engineering, Data Science.
    - \U0001F5FA\uFE0F Web Development: HTML, PHP, CSS, PL/SQL.
    - \U0001F4C8 Databases: Familiarity with PostgreSQL, MongoDB, MySQL.
    - \U0001F4A1 Backend: REST APIs, NoSQL, and FastAPI.
    """
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1 ---
st.write("\U0001F6E0\uFE0F", "**Virtual Software Engineer | JPMorgan Chase**")
st.write("April 2024, Remote")
st.write(
    """
    - Fixed broken repository files to ensure accurate web application outputs.
    - Used the Perspective library to create a live data visualization for trader monitoring.
    - Set up the development environment and managed dependencies.
    """
)

# --- JOB 2 ---
st.write('\n')
st.write("\U0001F6E0\uFE0F", "**Artificial Intelligence Intern | Infosys SpringBoard**")
st.write("December 2024, Remote")
st.write(
    """
    -Built a personalized chatbot for a Learning Management System using Rasa and optimized API integrations with Postman.
    - Gained experience with AI frameworks like TensorFlow.
    """
)

# --- TECHNICAL WRITING ---
st.write('\n')
st.subheader("Technical Writing")
st.write("---")
st.write(
    """
    - Authored technical articles on Medium, focusing on machine learning, data structures, and Python best practices.
    - [Explore My Articles on Medium](https://medium.com/@bishty2005).
    """
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"[\U0001F3C6 {project}]({details['link']})")
    st.write(details['description'])

# --- VOLUNTEERING ---
st.write('\n')
st.subheader("Clubs and Societies")
st.write(
    """
    - \U0001F91D Volunteer at IEEE JIIT Noida in the Public Relations Department.
    - \U0001F483 Member of Nrityang, the cultural dance society at JIIT.
    """
)

# --- ACHIEVEMENTS ---
st.write('\n')
st.subheader("Achievements")
st.write(
    """
    - Solved 350+ questions on Leetcode.
    - Participated in Google Cloud GenAI Study Jam.
    - Developed GenAI Apps with Gemini and Streamlit.
    - Earned Data Analytics Certification by Microsoft and LinkedIn.
    """
)

# --- LEETCODE STATS (Optional Widget) ---
st.write('\n')
st.subheader("LeetCode Progress")
st.write("---")
st.write("[Check My LeetCode Stats](https://leetcode.com/bishty2005)")
