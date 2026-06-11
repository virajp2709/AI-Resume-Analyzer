import streamlit as st
from PyPDF2 import PdfReader
st.title("AI Resume Analyzer")
uploaded_file = st.file_uploader(
    "Upload Resume", 
    type=["pdf"]
)
if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text= ""
    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
          text +=page_text
    st.subheader("Resume Content")
    st.write(text)
    skills = [
    "excel",
    "powerpoint",
    "data analysis",
    "communication",
    "content creation",
    "prompt engineering",
    ]
    found_skills = []
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    st.subheader("Detected Skills")
    for skill in found_skills:
        st.success(skill)
    score = len(found_skills) * 10
    if score > 100:
        score = 100 
    st.subheader("Resume Score")
    st.progress(score/100)
    st.write(f"Score: {score}/100")
    required_skills = [
        "python",
        "sql",
        "machine learning",
        "numPy",
        "pandas",
        "github",
    ]
    missing_skills = []
    for skill in required_skills:
        if skill.lower() not in text.lower():
            missing_skills.append(skill)
    st.subheader("Recommended Skills to Learn")
    for skill in missing_skills:
        st.warning(skill)
    if score >= 80:
        st.success("Excellent Resume ⭐⭐⭐⭐⭐")
    elif score >= 60:
        st.info("Good Resume ⭐⭐⭐⭐")
    elif score >= 40:
        st.warning("Average Resume ⭐⭐⭐")
    else:
        st.error("Needs Improvement ⭐⭐")
    st.subheader("Strengths")
    for skill in found_skills:
        st.success(f"✅ {skill}")
    if "project" in text.lower():
        st.success("Projects section found")
    else:
        st.warning("Add Projects Section")

