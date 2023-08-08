import os
import shutil

from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain.chains import ChatVectorDBChain
from PyPDF2 import PdfReader

# #Define API Key
# import sys
# sys.path.append('./OpenAI/')  
# from creds import openai_api_type, openai_api_version, openai_api_base, api_key
# #Define variables For Azure
# #---------  
# os.environ["OPENAI_API_TYPE"] = openai_api_type
# #os.environ["OPENAI_API_VERSION"] = "2022-12-01"
# os.environ["OPENAI_API_VERSION"] = openai_api_version
# os.environ["OPENAI_API_BASE"] = openai_api_base
# os.environ["OPENAI_API_KEY"] = api_key   
# #---------

# filePath = "./pdfs"
# inputFilePaths = [
#     "JSW ENERGY LTD Q1 FY2024.pdf",
#     "STERLING AND WILSON RENEWABLE Q1 FY2024.pdf"    
#     ]

# persist_directory="./Chroma/" 

# def remove_all_files(folder_path):
#     for root, _, file_names in os.walk(folder_path, topdown=False):
#         for file_name in file_names:
#             file_path = os.path.join(root, file_name)
#             os.remove(file_path)

# print('Generating Summaries')
# for inputFilePath in inputFilePaths:    
#     try:
#         # Call the function to remove all files
#         remove_all_files(persist_directory)
#         # Delete the index folder within the persist_directory
#         index_folder_path = f"{persist_directory}/index"
#         shutil.rmtree(index_folder_path)
#     except:
#         pass
    
#     pdfReader = PdfReader(open(filePath+"\\"+inputFilePath, 'rb'))
#     text=''
#     for i in range(0,len(pdfReader.pages)):
#         pageObj = pdfReader.pages[i]
#         text=text+pageObj.extract_text()
        
#     pdf_doc = TokenTextSplitter(chunk_size=1000, chunk_overlap=0).split_text(text)
#     embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1)    
#     vectordb2 = Chroma.from_texts(pdf_doc, embeddings, persist_directory=persist_directory,metadatas=[{"source": f"{inputFilePath}"} for pdf_doc_len in range(len(pdf_doc))])        
#     vectordb2.persist()  
    
#     pdf_qa = ChatVectorDBChain.from_llm(AzureChatOpenAI(temperature=0, deployment_name="GPTturbo3_5"), vectordb2, return_source_documents=True)    
#     query = f'{inputFilePath} is an earnings call transcript. Generate a summary of the document in 10 bullet points.'    
#     result = pdf_qa({"question": query, "chat_history": ''})
    
#     print('-------------------------')
#     print(result['answer'])

print('-------------------------')
print('Done')


