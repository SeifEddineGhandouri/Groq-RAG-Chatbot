# 🚀 Arabic-Real-Estate-Document-Analyzer


An AI-powered Arabic real estate document analysis chatbot built with **Gradio** and **Groq LLMs**, using **Retrieval-Augmented Generation (RAG)** and a modern UI. Users can upload documents (PDF, Word, JSON, etc.) and ask questions based on the content — no setup beyond your Groq API key.

---

## 🌐 Technology Stack

### 🧠 Backend

| Layer           | Technology / Library                          | Purpose                                      |
|-----------------|------------------------------------------------|----------------------------------------------|
| **Python 3.8+** | Core language                                 | Main application logic                       |
| **LangChain**   | `langchain.vectorstores`, `embeddings`, `text_splitter` | Document processing, vector DB, embeddings   |
| **Chroma**      | In-memory vector store                        | Stores and retrieves document embeddings     |
| **HuggingFace Transformers** | `sentence-transformers/all-MiniLM-L6-v2` | Text embeddings for similarity search        |
| **Groq API**    | REST endpoint with OpenAI-compatible schema   | Fast inference using Groq-hosted LLMs        |
| **PyPDF2**      | PDF parser (optional)                         | Extract text from PDF files                  |
| **python-docx** | Word file parser (optional)                   | Extract text from DOCX documents             |
| **CSV / JSON**  | Built-in Python modules                       | Read and parse structured data               |

### 🎨 Frontend

| Layer         | Technology         | Purpose                                 |
|---------------|--------------------|------------------------------------------|
| **Gradio**     | UI framework       | Build web interface in Python            |
| **Custom CSS** | Styling            | Modern layout, colors, responsiveness    |
| **Gradio Blocks API** | UI layout  | Organize inputs, file upload, chat UI    |
| **Responsive Design** | CSS media queries | Mobile-friendly layout               |

---

## ✅ Supported Groq LLM Models

| Model Name                                  | Type            | Description                          |
|---------------------------------------------|------------------|--------------------------------------|
| `llama-3.1-8b-instant`                      | Meta LLaMA 3     | Lightweight, fast inference          |
| `llama-3.1-70b-versatile`                  | Meta LLaMA 3     | Larger context, more capable         |
| `llama-3.3-70b-versatile`                  | Meta LLaMA 3.3   | Updated with better performance      |
| `mixtral-8x7b-32768`                       | Mistral (MoE)    | Long context, mixture-of-experts     |
| `gemma2-9b-it`                             | Google Gemma     | Instruction-tuned model              |
| `llama3-groq-70b-8192-tool-use-preview`    | Meta + tools     | Advanced capabilities (tool use)     |
| `llama3-groq-8b-8192-tool-use-preview`     | Meta + tools     | Smaller preview model                |

---

## 🔍 Features

- 📂 Upload and parse `.pdf`, `.docx`, `.txt`, `.csv`, `.json`
- 🧠 Ask questions using context-aware RAG retrieval
- 📊 Real-time document preview and status updates
- 🪄 Supports Groq's fastest inference LLMs via simple API key
- 🖼 Clean, responsive modern UI (dark mode compatible)
- 🔐 Secure: no data stored or sent to external servers

---

## 📦 Requirements

To install all required Python packages, run:

```sh
pip install -r requirements.txt
```

This will install:
- gradio
- requests
- langchain
- chromadb
- sentence-transformers
- PyPDF2
- pdfplumber
- pdf2image
- pytesseract
- python-docx
- pandas
- pillow

**System requirements:**

- [Tesseract OCR (Windows build by UB Mannheim)](https://github.com/UB-Mannheim/tesseract/wiki)  
  Download and install. Add the install path (e.g., `C:\Program Files\Tesseract-OCR`) to your system PATH.
  - For Arabic OCR, download [ara.traineddata](https://github.com/tesseract-ocr/tessdata) and place it in your Tesseract `tessdata` folder (e.g., `C:\Program Files\Tesseract-OCR\tessdata`).
- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)  
  Download and extract. Add the following to your system environment variables:
  - `C:\poppler-24.08.0\Library\bin` (or your Poppler bin path) to your PATH.

**How to set environment variables (Windows):**
1. Open System Properties > Advanced > Environment Variables.
2. Under "System variables", find and edit the `Path` variable.
3. Add:
   - `C:\Program Files\Tesseract-OCR`
   - `C:\poppler-24.08.0\Library\bin`
4. Click OK and restart your terminal/PC if needed.

**Summary of all dependencies:**
- gradio
- requests
- langchain
- chromadb
- sentence-transformers
- PyPDF2
- pdfplumber
- pdf2image
- pytesseract
- python-docx
- pandas
- pillow

These packages and tools ensure your chatbot works with all supported file types, scanned/image PDFs, and RAG features.


