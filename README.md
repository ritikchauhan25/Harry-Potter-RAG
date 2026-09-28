# Harry Potter RAG Chatbot

A Retrieval-Augmented Generation (RAG) application built with **Python, LangChain, Google Gemini, Chroma, and Gradio**.

The project loads a Harry Potter narrative text document, splits it into chunks, creates vector embeddings, stores them in Chroma, retrieves relevant context for a question, and uses Google Gemini to generate a context-grounded answer.

## Project Title

**GenAI / RAG Application | Python, LangChain, Gemini, Chroma**

## Architecture

```text
Harry Potter TXT Document
          |
          v
     TextLoader
          |
          v
RecursiveCharacterTextSplitter
  500-character chunks
  200-character overlap
          |
          v
Google Gemini Embeddings
 gemini-embedding-001
          |
          v
      Chroma Vector Store
          |
          v
       Chroma Retriever
          |
          v
    Retrieved Context
          |
          v
   Google Gemini LLM
    gemini-3.8-flash
          |
          v
      Final Answer
          |
          v
      Gradio Chat UI
```

## Features

- Document loading with LangChain `TextLoader`
- Recursive character-based text splitting
- 500-character chunk size
- 200-character chunk overlap
- Google Gemini document embeddings
- Chroma vector database
- Semantic retrieval through a Chroma retriever
- Context-grounded response generation with Gemini
- Interactive Gradio chatbot
- Original working Jupyter/Colab notebook included

## Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | RAG pipeline orchestration |
| Google Gemini | Embeddings and LLM |
| Chroma | Vector storage and retrieval |
| Gradio | Chatbot interface |
| Jupyter Notebook | Experimentation and development |

## Project Structure

```text
Harry-Potter-RAG/
│
├── app.py
├── RAGHandson-Rithik.ipynb
├── data/
│   └── harrypotter.txt
├── requirements.txt
├── .env.example
├── .gitignore
├── Screenshot 2026-09-28 154259.png
└── README.md
```

## Demo

The application provides a Gradio-based chatbot interface for asking questions about the supplied Harry Potter narrative document.

![Harry Potter RAG Chatbot Demo](Screenshot%202026-09-28%20154259.png)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ritikchauhan25/Harry-Potter-RAG.git
cd Harry-Potter-RAG
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google API key

Create a `.env` file from `.env.example`.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Then edit `.env`:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

**Never commit your `.env` file or expose your API key on GitHub.**

### 5. Run the chatbot

```bash
python app.py
```

Gradio will provide a local URL in the terminal.

## Example Questions

Try questions such as:

```text
Who is Harry Potter?
```

```text
What happened in the Chamber of Secrets?
```

```text
Who is Sirius Black?
```

```text
What are Horcruxes?
```

```text
What happened to Dumbledore?
```

```text
What are the core themes of the story?
```

The chatbot is designed to answer from the supplied document context.

## Jupyter / Colab Version

`RAGHandson-Rithik.ipynb` contains the original hands-on implementation.

The notebook uses:

- `TextLoader`
- `RecursiveCharacterTextSplitter`
- `GoogleGenerativeAIEmbeddings`
- `Chroma`
- `ChatGoogleGenerativeAI`
- LangChain prompt and runnable components
- `Gradio ChatInterface`

The notebook's original document path was a Google Colab path. The included `app.py` adapts the same workflow to the GitHub repository's local `data/harrypotter.txt` path.

## Resume Description

> **GenAI / RAG Application | Python, LangChain, Gemini, Chroma**
> Built a Retrieval-Augmented Generation application over a Harry Potter narrative TXT document using Recursive Character Text Splitting with 500-character chunks and 200-character overlap. Generated document embeddings using Google Gemini and stored them in Chroma for semantic retrieval. Implemented vector-based document retrieval and integrated Google Gemini for context-grounded responses. Developed an interactive Gradio chatbot for document question answering.

## Notes

This repository contains the project document used for the RAG demonstration. For public distribution, make sure you have the appropriate rights to redistribute any source material you upload.

## Author

**Ritik Chauhan**

Data Scientist | Python | SQL | Machine Learning | Generative AI

GitHub: https://github.com/ritikchauhan25
