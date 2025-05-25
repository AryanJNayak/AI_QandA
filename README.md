# 📄 Talk with PDF

A simple yet powerful PDF Question-Answering app built using **Streamlit**, **Google Gemini LLM**, and **LlamaIndex**. Upload any PDF, ask natural language questions, and get context-aware answers instantly.

> Hosted locally and tunneled via **Ngrok** for public access.


> [![Demo Video](https://drive.google.com/uc?export=view&id=1W0R6ge-6wlbOsK9d1y4PIBkVhIn4AUks)](https://drive.google.com/file/d/1lAS0czenHQC93V_26JKW34lnCCAoBFam/view)
---

## 🚀 Features

- 📁 Upload your own PDFs
- 💬 Ask questions in natural language
- ⚡ Powered by Google Gemini 1.5 Flash
- 🧠 LlamaIndex for document indexing
- 🌐 Public access via Ngrok tunnel

---

## 📁 Project Structure

pdf-qa-app/  
├── app.py # Streamlit app  
├── tunnel.py # Ngrok tunnel + app launcher  
├── .env # Stores API keys (not pushed to Git)  
├── Data/ # Folder for uploaded PDFs  
└── requirements.txt # Dependencies  

---

## 🔐 .env Example

Create a `.env` file in the root with:
```
GOOGLE_API_KEY=your_google_api_key

NGROK_TOKEN=your_ngrok_token
```
---

## 🧪 Run Locally

1. **Install dependencies**:

```
pip install -r requirements.txt
```
2. Run the app:
```
python tunnel.py
```

3. Visit the Ngrok URL shown in the terminal.

---
## 📦 Requirements
Python 3.8+

Streamlit

pyngrok

python-dotenv

llama-index

Google Gemini API access
