import os
import sys
import gradio as gr
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def load_and_split(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    loader = TextLoader(filepath, encoding="utf-8")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=200
    )
    return splitter.split_documents(docs)

def create_rag_chain(splits):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        task_type="retrieval_document"
    )

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings
    )
    retriever = vectorstore.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0
    )

    template = """Answer the question based only on the following context:
{context}

Question: {question}

Helpful Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

def main():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError(
            "GOOGLE_API_KEY is not set. Create a .env file from .env.example."
        )

    filepath = os.path.join("data", "harrypotter.txt")
    splits = load_and_split(filepath)
    rag_chain = create_rag_chain(splits)

    def respond(message, chat_history):
        try:
            return rag_chain.invoke(message)
        except Exception as exc:
            return f"An error occurred: {exc}"

    demo = gr.ChatInterface(
        fn=respond,
        textbox=gr.Textbox(
            placeholder="Ask a question related to Harry Potter",
            container=False,
            scale=7
        ),
        title="Harry Potter RAG Chatbot",
        description=(
            "Ask questions about the supplied Harry Potter narrative document. "
            "Answers are generated from retrieved document context."
        )
    )

    demo.launch()

if __name__ == "__main__":
    main()
