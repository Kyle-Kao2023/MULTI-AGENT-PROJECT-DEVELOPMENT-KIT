#!/usr/bin/env python3
# --- Wave 2 Feature: Knowledge Base Builder ---

from pathlib import Path

# (Wave 2) Import necessary libraries when implemented:
# from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# Define paths
PLAN_DOCS_PATH = Path("docs/plan")
# In a real scenario, we'd also load PR summaries, backtest reports etc.
VECTOR_STORE_PATH = Path("artifacts/vector_store")
INDEX_NAME = "faiss_index"

def build_knowledge_base():
    """
    (Not Implemented - Wave 2)
    This script will build a vector store knowledge base from project documents.
    
    Workflow:
    1. Load documents from specified directories (docs/plan, etc.).
    2. Split documents into manageable chunks for embedding.
    3. Use an embedding model to convert text chunks into vectors.
    4. Store the vectors in a FAISS index for efficient retrieval.
    5. Save the FAISS index locally.
    """
    print("--- Knowledge Base Builder (Wave 2 - Not Implemented) ---")
    
    # --- Step 1: Initialize components (Wave 2) ---
    # embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    # --- Step 2: Load documents (Wave 2) ---
    print(f"1. Scanning for documents in '{PLAN_DOCS_PATH}'...")
    # loader = DirectoryLoader(PLAN_DOCS_PATH, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    # docs = loader.load()
    # if not docs:
    #     print("No documents found. Nothing to build.")
    #     return
    
    # --- Step 3: Split documents (Wave 2) ---
    # print(f"2. Splitting {len(docs)} documents into chunks...")
    # chunks = text_splitter.split_documents(docs)
    
    # --- Step 4: Create and save vector store (Wave 2) ---
    # print(f"3. Creating vector store from {len(chunks)} chunks...")
    # vector_store = FAISS.from_documents(chunks, embeddings)
    # VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)
    # vector_store.save_local(folder_path=str(VECTOR_STORE_PATH), index_name=INDEX_NAME)
    
    print("\nFunctionality to be implemented in Wave 2.")
    print(f"When implemented, this will create a vector store at: '{VECTOR_STORE_PATH / INDEX_NAME}'")
    print("--- End ---")

if __name__ == "__main__":
    build_knowledge_base()
