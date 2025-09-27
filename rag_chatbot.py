import os
from dotenv import load_dotenv
from pathlib import Path

# LangChain & Pinecone
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore 
from pinecone import Pinecone, ServerlessSpec

# Groq LLM
from langchain_groq import ChatGroq

load_dotenv()


class ChatBot:
    def __init__(
        self,
        doc_path: str = "./Data/Bangalore_travel_assistant.txt",
        pinecone_index: str = "langchain-bangalore",
        embedding_model_name: str = "all-MiniLM-L6-v2",
        chunk_size: int = 1000,
        chunk_overlap: int = 50,
        top_k: int = 4,
    ):
        self.doc_path = doc_path
        self.index_name = pinecone_index
        self.top_k = top_k

        # 1. Load and split documents
        if not Path(self.doc_path).exists():
            raise FileNotFoundError(f"Document not found: {self.doc_path}")

        loader = TextLoader(self.doc_path, encoding="utf-8")
        documents = loader.load()

        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        docs = text_splitter.split_documents(documents)

        # 2. Embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

        # 3. Pinecone (new SDK)
        PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        PINECONE_ENV = os.getenv("PINECONE_ENV")

        if not PINECONE_API_KEY or not PINECONE_ENV:
            raise ValueError("Missing PINECONE_API_KEY or PINECONE_ENV in .env")

        pc = Pinecone(api_key=PINECONE_API_KEY)

        # Create index if not exists
        if self.index_name not in pc.list_indexes().names():
            embedding_dim = len(self.embeddings.embed_query("test"))
            pc.create_index(
                name=self.index_name,
                dimension=embedding_dim,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV),
            )

        # 4. Vector Store (langchain-pinecone)
        self.vectorstore = PineconeVectorStore.from_documents(
            docs,
            self.embeddings,
            index_name=self.index_name,
            namespace="travel-assistant"
        )

        # 5. LLM: Groq + LLaMA 3.1
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        if not GROQ_API_KEY:
            raise ValueError("Missing GROQ_API_KEY in .env")

        self.llm = ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.1-13b-versatile"),
            api_key=GROQ_API_KEY,
            temperature=float(os.getenv("GROQ_TEMPERATURE", 0.2)),
            max_tokens=int(os.getenv("GROQ_MAX_TOKENS", 512))
        )

        # 6. Prompt + RAG Chain
        template = """You are a helpful Bangalore travel assistant with answers grounded strictly in the provided context.
If the context does not contain the answer, reply with "I don't know" or provide best-effort guidance, but prefer to state unknown.
Keep answers short and concise (no more than 2 sentences) unless a longer answer is requested.

Context:
{context}

Question:
{question}

Answer (concise):
"""
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])

        retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": self.top_k})

        self.rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": prompt}
        )

    def answer(self, user_query: str) -> str:
        return self.rag_chain.run(user_query)


if __name__ == "__main__":
    bot = ChatBot()
    print(bot.answer("What are must-try foods in Bangalore?"))
