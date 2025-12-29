# 📚 PDF AI – Ask Questions From Any PDF

A simple AI tool where you can upload a PDF and ask questions — and it answers based only on the document.  
Built using **Python + Streamlit + Groq AI**.

Perfect for:
- Students 📖
- Researchers 🧠
- Professionals 📂
- Anyone who doesn’t want to manually read huge PDFs 😅


## ✨ Features
✔ Upload any PDF  
✔ Ask natural-language questions  
✔ AI answers using PDF content only  
✔ Simple & clean UI  
✔ Fast and lightweight  
✔ Secure (API key hidden)


## 🛠 Tech Used
- Python
- Streamlit (Web UI)
- PyPDF2 (PDF text extraction)
- Groq API (AI brain)


## 🚀 Run Locally

### 1️⃣ Clone the Repo
git clone https://github.com/SHAILUV-prog/pdfai.git
cd pdfai

### 2️⃣ Install Requirements
pip install -r requirements.txt

### 3️⃣ Add Groq API Key
Get your API key from:
https://console.groq.com

Then set:
Windows:
setx GROQ_API_KEY "your_api_key_here"

Mac/Linux:
export GROQ_API_KEY="your_api_key_here"

### 4️⃣ Run the App
streamlit run app.py

Your browser will open automatically 🎉


## 🌍 Deploy to Streamlit Cloud (Free)

1️⃣ Push project to GitHub  
2️⃣ Go to https://share.streamlit.io  
3️⃣ Click "Deploy App"  
4️⃣ Select your repo  
5️⃣ Select `app.py`  
6️⃣ Add Secrets:
GROQ_API_KEY = your_api_key_here

Done 🎯 You will get a public website link.


## 📁 Project Structure
pdfai/
 ├── app.py
 ├── requirements.txt
 └── README.md


## ❤️ Why This Project?
Reading long PDFs is boring and time-consuming 😭  
So this project turns any PDF into a **smart assistant** that answers questions like a human.

