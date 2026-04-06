import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_ats
from job_roles import JOB_ROLES

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🧠 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])
job_role = st.selectbox("Select Job Role", JOB_ROLES.keys())

if uploaded_file:
    text = extract_text(uploaded_file)
    resume_skills = extract_skills(text)
    job_skills = JOB_ROLES[job_role]

    ats, matched = calculate_ats(resume_skills, job_skills)
    missing = list(set(job_skills) - set(matched))

    st.subheader("📌 Extracted Skills")
    st.write(resume_skills)

    st.subheader("📊 ATS Score")
    st.progress(int(ats))
    st.write(f"ATS Score: {ats}%")

    st.subheader("✅ Matched Skills")
    st.success(matched)

    st.subheader("❌ Missing Skills")
    st.error(missing)
