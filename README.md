# 🎯 Interview Practice Bot

A beginner-friendly AI chatbot that helps you practice technical interviews on Python and GenAI topics.

## Features

- Choose from **Python**, **GenAI Fundamentals**, **RAG**, and **AI Agents** topics
- Get AI-generated interview questions on demand
- Submit answers and receive structured feedback — score, what was correct, what was missed, and a model answer
- Ask follow-up questions with full conversation memory
- Click **New Question** anytime to reset and start fresh

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Add your Gemini API key**

Open `.env` and replace the placeholder:
```
GOOGLE_API_KEY=your_actual_key_here
```
Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

**3. Run the app**
```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Project Structure

```
interview-bot/
├── app.py          # Streamlit UI and app flow
├── agent.py        # LangChain + Gemini API calls
├── prompts.py      # All prompt templates
├── .env            # Your API key — never commit this
├── requirements.txt
└── README.md
```

## How It Works

| File | Responsibility |
|---|---|
| `prompts.py` | Three prompt templates: question generation, answer scoring, follow-up |
| `agent.py` | `generate_question()`, `score_answer()`, `handle_followup()` — each is a direct LangChain model call |
| `app.py` | Streamlit UI, `st.session_state` management, and routing between scoring vs. follow-up mode |

## Model

Uses `gemini-2.5-flash-lite` via `langchain-google-genai`. To swap to a different model, change the `model=` value in `agent.py → get_model()`.
