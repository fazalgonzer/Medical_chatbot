
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
def load_data(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    docs= loader.load()
    return docs


def text_split(extracted_data):
   text_splitter= RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
   text_chunk=text_splitter.split_documents(extracted_data)
   return text_chunk


def embedding_models(model_name:str):
    embedding_model=HuggingFaceEmbeddings(model_name=model_name)
    
    return embedding_model