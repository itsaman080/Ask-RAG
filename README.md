# AskRAG – AI-Powered Retrieval-Augmented Generation Chatbot

**AskRAG** is a **Retrieval-Augmented Generation (RAG)** chatbot framework that allows you to build AI assistants for **any domain** using a knowledge base. In this repository, we demonstrate it with a **Bangalore travel assistant**, but the system is generic and can be adapted to other topics.

The bot leverages **document embeddings**, **Pinecone vector database**, and **Groq LLaMA 3.1** for generating context-aware answers.

---

## 🧭 Features

- Upload and split text documents to create a knowledge base.
- Automatically generate embeddings and store them in **Pinecone**.
- Retrieve context using **vector similarity search**.
- Generate concise, context-grounded answers with **Groq LLaMA 3.1**.
- Streamlit-based interactive chat interface.
- Session-based chat history.
- Handles unknown queries gracefully.
- Easily extendable to **any domain** by replacing the text documents.

---

## 🛠 Tech Stack

| Component        | Technology                               |
|-----------------|-----------------------------------------|
| Frontend        | Streamlit                                |
| Backend         | Python 3.10                              |
| Embeddings      | HuggingFace `all-MiniLM-L6-v2`          |
| Vector Database | Pinecone (Serverless Index)              |
| LLM             | Groq LLaMA 3.1 via `langchain_groq`     |
| Document Loader | `langchain_community.document_loaders`  |
| Environment     | `python-dotenv`                          |

---

## 📂 Project Structure

```

AskRAG/
├─ Data/
│  └─ Bangalore_travel_assistant.txt    # Sample knowledge base
├─ env/                                  # Python virtual environment
├─ rag_chatbot.py                        # Chatbot class, embeddings & RAG logic
├─ streamlit_app.py                      # Streamlit interface
├─ .env                                  # API keys for Pinecone and Groq
├─ requirements.txt                      # Python dependencies
└─ README.md                             # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/itsaman080/AskRAG.git
cd AskRAG
````

### 2. Create and activate a Python virtual environment

```bash
virtualenv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
PINECONE_API_KEY=<your-pinecone-api-key>
PINECONE_ENV=<your-pinecone-environment>  # e.g., us-east-1
GROQ_API_KEY=<your-groq-api-key>
GROQ_MODEL=llama-3.1-13b-versatile
GROQ_TEMPERATURE=0.2
GROQ_MAX_TOKENS=512
```

> **Note:** Replace the sample keys with your actual API credentials. The `GROQ_MODEL` key can be changed if you have access to a different LLaMA variant.

---

## 🚀 Running the Application

```bash
streamlit run streamlit_app.py
```

* Open the displayed URL in your browser (usually `http://localhost:8501`).
* Chat with the bot using the sample knowledge base or your own documents.

---

## 🧩 How It Works

1. **Document Processing:**
   Text files are loaded, split into smaller chunks, and embedded using HuggingFace embeddings.

2. **Vector Storage:**
   Embeddings are stored in a Pinecone index. If the index does not exist, it is automatically created.

3. **Retrieval:**
   For a user query, the bot retrieves the top-K most relevant document chunks using similarity search.

4. **Answer Generation:**
   The retrieved context is passed to Groq LLaMA 3.1 for generating a concise answer.

5. **Chat Interface:**
   Streamlit displays chat history and allows ongoing interaction.

---

## 🌏 Extending to Other Domains

1. Replace the sample `Bangalore_travel_assistant.txt` file with your own text documents.
2. Update `doc_path` in `streamlit_app.py` or `.env` as needed.
3. Restart the Streamlit app — embeddings will be generated for the new documents and stored in Pinecone.

---

## ⚠️ Known Issues / Tips

* Make sure you have access to the LLaMA 3.1 model via Groq API.
* Pinecone serverless indices may take a few seconds to initialize on first run.
* Large documents may take longer to embed; consider splitting documents wisely.
* HuggingFace deprecation warnings can be ignored for now, but consider migrating to `langchain-huggingface` package in future.

---

## 📖 References

* [LangChain](https://www.langchain.com/)
* [Pinecone Vector DB](https://www.pinecone.io/)
* [Groq LLaMA API](https://www.groq.com/)

---

## 🔮 Future Enhancements

* Add support for **multi-document uploads**.
* Integrate additional **real-time data sources** (Wikipedia, news APIs, etc.).
* Support **multi-turn conversation memory**.
* Add **web-based admin panel** for dynamic knowledge base updates.

