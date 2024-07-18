from flask import Flask,render_template,jsonify,request
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from src.prompt import prompt_template
from src.helper import *
import os 
from langchain_groq import ChatGroq
app=Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
embeddings=embedding_models("BAAI/bge-small-en-v1.5")


llm=ChatGroq(groq_api_key="",
             model_name="Llama3-8b-8192")
new_db = FAISS.load_local("Vector/faiss_index", embeddings,allow_dangerous_deserialization=True)
prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
chain_kwargs={"prompt":prompt}
qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=new_db.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_kwargs)

result=""

@app.route("/")
def index():

    return render_template("chat.html",notification="Flask working")



@app.route("/upload",methods=['POST'])
def Query():
    user_input = request.form['user_input']
    result=qa({"query":user_input})



    return render_template("chat.html",notification=result["result"])




if __name__=='__main__':
    app.run(debug=True)
