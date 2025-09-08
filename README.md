# 📖 AskRAG - Chatbot

**AskRAG** is a simple Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **Streamlit**, **Pinecone**, and **OpenAI**.
It demonstrates how to combine a vector database with a Large Language Model (LLM) to create a chatbot that can answer domain-specific questions with higher accuracy and reduced hallucination.

---

## 🚀 Features

* 🔹 **RAG Pipeline** → retrieval + generation for more accurate answers
* 🔹 **Streamlit Frontend** → clean, interactive web UI
* 🔹 **LangChain** → orchestration of prompt, retriever, and LLM
* 🔹 **Pinecone** → scalable vector storage & retrieval
* 🔹 **OpenAI API** → embeddings + natural language understanding

---

## 🛠️ Tech Stack

* **Frontend** → Streamlit
* **Backend** → LangChain
* **LLM** → OpenAI GPT models
* **Vector Database** → Pinecone

---

## 📂 Project Structure

```
Ask-RAG/
│── src/
│   ├── RAG_ChatBot.py        # Chatbot class (retrieval + generation pipeline)
│   ├── streamlitMain.py      # Streamlit frontend
│   ├── materials/            # Knowledge base (text/PDF files)
│── .env                      # API keys (OpenAI & Pinecone)
│── requirements.txt          # Dependencies
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
```

---

## ⚙️ Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/itsaman080/Ask-RAG.git
   cd Ask-RAG
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add data**
   Place your domain-specific documents (e.g., travel guides, policies) inside the `src/materials/` folder.

---

## ▶️ Running the Chatbot

Run the Streamlit app:

```bash
cd src
streamlit run streamlitMain.py
```

Open the provided URL (default: `http://localhost:8501`) to chat with **AskRAG**.

---

## 📊 How It Works

1. **Data Preparation** → documents are chunked and converted into embeddings.
2. **Indexing** → embeddings are stored in Pinecone.
3. **Retrieval** → relevant chunks are fetched based on user queries.
4. **Prompt Engineering** → retrieved context + query form the final LLM prompt.
5. **Generation** → OpenAI LLM produces a context-aware answer.


---

## 📜 License

MIT License.
