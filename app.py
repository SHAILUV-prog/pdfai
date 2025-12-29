import os
import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq

st.set_page_config(page_title="PDF Q/A", page_icon="📚", layout="centered")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("📚 PDF Question Answering")
st.write("Upload a PDF and ask any question from it.")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_pdf:
    st.info("Reading PDF… Please wait")
    pdf_text = extract_text(uploaded_pdf)
    st.success("PDF Loaded Successfully 🎉")

    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if not pdf_text.strip():
            st.error("PDF has no readable text.")
        else:
            try:
                with st.spinner("Thinking…"):
                    prompt = f"Answer the question using ONLY the content from this PDF:\n\n{pdf_text}\n\nQuestion: {question}"

                    response = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=500
                    )

                    answer = response.choices[0].message.content

                st.subheader("Answer")
                st.write(answer)

            except Exception as e:
                st.error("Something went wrong")
                st.code(str(e))
