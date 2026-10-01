import streamlit as st
import PyPDF2

def input_pdf_text(uploaded_file) -> str:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

st.title("Smart ATS - Resume Expert")

job_description = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload your resume PDF", type=["pdf"])

if st.button("Analyze Resume"):
    if uploaded_file is not None:
        pdf_text = input_pdf_text(uploaded_file)
        st.write(pdf_text)
    else:
        st.warning("Please upload a PDF file before submitting.")
