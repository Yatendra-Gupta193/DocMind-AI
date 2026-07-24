# 🚀 DocMind AI   
 
An AI-powered document question answering application built using **FastAPI**, **LangChain**, **ChromaDB**, **OpenAI Embeddings**, **Mistral AI**, and **Next.js**.

DocMind AI allows users to upload a PDF and ask natural language questions about its contents. It uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant document chunks and generate grounded answers with source citations.

---

# 🌐 Live Application:  https://doc-mind-ai-green.vercel.app/

---

## 📸 Screenshots

### 🏠 Landing Page

![Landing Page](assets/1.png)

---

### 💬 Main Chat Interface

![Main Interface](assets/2.png)

![Main Interface](assets/3.png) 

---

# ✨ Features

- 📄 Upload your own PDF documents
- 🤖 AI-powered document question answering
- 🔍 Semantic search using OpenAI Embeddings
- 📚 ChromaDB Vector Database
- 🧠 Retrieval-Augmented Generation (RAG)
- 📍 Source citations with page numbers
- ⚡ FastAPI REST API
- 🎨 Modern responsive Next.js frontend
- 🌙 Clean professional dark UI
- ☁️ Cloud deployment (Render + Vercel)
- ❌ Prevents hallucinations by answering only from uploaded documents

---

# 🏗️ System Architecture

```
                User Uploads PDF
                        │
                        ▼
                PyPDFLoader
                        │
                        ▼
     RecursiveCharacterTextSplitter
                        │
                        ▼
          OpenAI Embeddings Model
                        │
                        ▼
                  ChromaDB
                        │
                        ▼
                MMR Retriever
                        │
                        ▼
      Prompt + Retrieved Context
                        │
                        ▼
                 Mistral AI
                        │
                        ▼
     Answer + Source Citations
```

---

# ⚙️ Tech Stack

## Backend

- Python
- FastAPI
- LangChain
- ChromaDB
- OpenAI Embeddings (`text-embedding-3-small`)
- Mistral AI
- PyPDFLoader

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

## Deployment

- Render
- Vercel

---

# 📂 Project Structure

```
DocMind-AI/

├── assets/
│
├── backend/
│
├── frontend/
│
├── .gitignore/
│
└── README.md
```

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/Rishabh150102/DocMind-AI.git

cd DocMind-AI
```

---

## Backend

```bash
cd backend

python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
OPENAI_API_KEY=YOUR_KEY

MISTRAL_API_KEY=YOUR_KEY
```

Run

```bash
uvicorn api:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install
```

Create

```
.env.local
```

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Run

```bash
npm run dev
```

---

# 📌 API Endpoints

## Upload Document

```
POST /upload
```

Uploads and indexes a PDF into the vector database.

---

## Chat

```
POST /chat
```

Returns

```json
{
    "answer": "...",
    "sources": [
        {
            "page": 4,
            "source": "sample.pdf"
        }
    ]
}
```

---

# 💡 Engineering Highlights

This project was built with a focus on production-oriented RAG architecture.

Highlights include:

- Dynamic PDF upload and indexing
- Semantic retrieval using MMR
- Grounded AI responses
- Source citations with page numbers
- Modular backend architecture
- Environment-based configuration
- Responsive frontend
- Independent frontend and backend deployment

---

# 🚧 Current Limitations

Current version supports:

- Single active document per session
- Text-based PDFs only

Planned future improvements:

- OCR support for scanned PDFs
- Multi-document retrieval
- User authentication
- Per-user vector databases
- Persistent chat history
- Streaming responses
- Background document processing
- Hybrid Search
- Reranking Pipeline

---

# 👨‍💻 Author : Yatendra Kumar Gupta

---

## ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub!# RAGDoc_Assistant
