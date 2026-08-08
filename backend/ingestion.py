import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv


start = time.time()

load_dotenv()


# Function for loading PDF
def load_file(file_path):
    loader = PyPDFLoader(file_path=file_path)
    document = loader.load()

    print(time.time() - start)
    return document


# Function for splitting document into chunks
def split_document(document):

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    ).split_documents(document)

    print(time.time() - start)
    return chunks


# Gemini Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=os.getenv("GEMINI_API_KEY")
)


# Function for creating vector store
def create_vector_store(chunks):

    print("Creating embeddings...")

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    # Reset ChromaDB
    if os.path.exists("chroma_db"):
        vectorstore.reset_collection()

    vectorstore.add_documents(chunks)

    print("Embeddings stored successfully")
    print("Stored in ChromaDB")
    print(time.time() - start)

    return vectorstore


# Function to delete uploaded file
def reset_knowledge_base():

    folder_path = "uploads"

    if os.path.exists(folder_path):

        contents = os.listdir(folder_path)

        if not contents:
            print("The folder is already empty. No action taken.")

        else:
            for item in contents:

                item_path = os.path.join(folder_path, item)

                if os.path.isfile(item_path):
                    os.remove(item_path)

            print("Uploaded file deleted.!!")

    return "Everything clear and ready to use."