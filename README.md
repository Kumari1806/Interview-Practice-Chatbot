# 🎯 AI Interview Practice Chatbot

An AI-powered Interview Practice Chatbot built using **Python**, **Streamlit**, **LangChain**, and **Google Gemini**. The application simulates a technical interview by generating topic-specific interview questions, evaluating user responses, providing structured feedback, and supporting context-aware follow-up conversations.

This project demonstrates the development of an AI-powered interview practice application using Streamlit, LangChain, and Google Gemini. It generates interview questions, evaluates user responses, provides structured feedback, and supports context-aware follow-up conversations.

---

## 🚀 Features

- Select an interview topic before starting a session
- AI-generated interview questions
- Chat-based interview experience
- Automatic answer evaluation
- Structured feedback including:
  - ⭐ Score (Out of 5)
  - ✅ What was Correct
  - ❌ What was Missed
  - 📖 Model Answer
- Context-aware follow-up conversations
- Session reset using **New Question**
- Conversation memory using Streamlit Session State

---

## 📚 Supported Topics

- Python
- GenAI Fundamentals
- Retrieval-Augmented Generation (RAG)
- AI Agents

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| UI Framework | Streamlit |
| LLM Framework | LangChain |
| LLM Provider | Google Gemini |
| Environment Variables | python-dotenv |

---

## 📂 Project Structure

```text
interview-bot/
│
├── app.py
├── agent.py
├── prompts.py
├── requirements.txt
├── README.md
└── .env
```

> **Note:** The `.env` file stores your API key and should never be committed to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kumari1806/Interview-Practice-Chatbot.git
```

### 2. Navigate to the project folder

```bash
cd Interview-Practice-Chatbot/interview-bot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure your API Key

Create a `.env` file inside the project directory.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

You can obtain a free API key from **Google AI Studio**.

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Application Workflow

```text
Select Topic
      │
      ▼
AI Generates Interview Question
      │
      ▼
User Submits Answer
      │
      ▼
AI Evaluates Response
      │
      ▼
Score + Feedback + Model Answer
      │
      ▼
Follow-up Questions (Conversation Memory)
      │
      ▼
New Question / New Session
```

---

## ⚙️ How It Works

| File | Responsibility |
|------|----------------|
| `prompts.py` | Contains prompt templates for question generation, answer evaluation, and follow-up conversations |
| `agent.py` | Handles Gemini model initialization, LangChain interactions, question generation, answer scoring, and follow-up responses |
| `app.py` | Manages the Streamlit user interface, session state, chat history, and overall application workflow |

---

## 🧠 AI Model

This project uses:

- **Google Gemini**
- **Model:** `gemini-2.5-flash-lite`
- **Framework:** `langchain-google-genai`

To use another Gemini model, update the model name inside `agent.py`.

---

## 📖 Concepts Demonstrated

- Large Language Models (LLMs)
- LangChain Integration
- Prompt Engineering
- Conversational AI
- Streamlit Chat Interface
- Session State Management
- Conversation Memory
- AI-based Answer Evaluation

---

## 🔮 Future Enhancements

- Difficulty level selection
- Interview history export
- RAG-powered interview question bank
- Additional interview domains
- Cloud deployment
- Enhanced memory strategies


