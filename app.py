
(import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
page_title="ExamGenius AI",
page_icon="🧠",
layout="wide"
)

st.title("🧠 EXAMGENIUS AI")
st.subheader("From Syllabus & Past Papers to Personalized Exam Preparation")

st.write(
"Upload your syllabus and past question papers to generate "
"an intelligent practice paper."
)

st.header("📚 Step 1: Upload Syllabus")

syllabus_file = st.file_uploader(
"Upload your syllabus PDF",
type=["pdf"]
