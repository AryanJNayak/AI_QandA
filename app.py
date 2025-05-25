import os
import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv

# Load .env for API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini LLM and Embedding
llm = GoogleGenAI(model="models/gemini-1.5-flash", api_key=api_key)
embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=api_key)

# Apply settings globally
Settings.llm = llm
Settings.embed_model = embed_model

st.title("📄 PDF QA App with Gemini + Streamlit")

# PDF Upload
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
if uploaded_file:
    os.makedirs("Data", exist_ok=True)
    file_path = os.path.join("Data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.success(f"Saved PDF to Data/{uploaded_file.name}")

    with st.spinner("Reading and indexing document..."):
        docs = SimpleDirectoryReader("Data").load_data()
        index = VectorStoreIndex.from_documents(docs)
        query_engine = index.as_query_engine()

    question = st.text_input("Ask a question about your PDF:")
    if question:
        with st.spinner("Answering..."):
            response = query_engine.query(question)
            st.write("🧠 Answer:", response.response)
