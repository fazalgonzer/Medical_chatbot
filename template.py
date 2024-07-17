import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")
list_of_files=[
   "src//__init__.py",
   "src/helper.py",
   "src/prompt.py",
   "setup.py",
   "requirements.txt",
   "research/trails.ipynb",
   "app.py",
   "store_index.py",
   "templates/chat.html",
   "static",


]
for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("created all the files{filedir}")
    if (not os.path.exists(file_path) or os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass 
            logging.info(f"created empty file as {file_path}")
    else:
        logging.info(f"{filename} is already exist at {file_path}") 



