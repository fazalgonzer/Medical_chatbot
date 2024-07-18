from src.helper import load_data,text_split,embedding_models
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

llm=ChatGroq(groq_api_key="",
             model_name="Llama3-8b-8192")

embeddings=embedding_models("BAAI/bge-small-en-v1.5")

new_db = FAISS.load_local("Vector/faiss_index", embeddings)