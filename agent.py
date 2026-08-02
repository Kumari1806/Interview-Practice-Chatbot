import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import FOLLOWUP_QUESTION_PROMPT, QUESTION_PROMPT, SCORING_PROMPT

load_dotenv()


def get_model(temperature: float = 0.7) -> ChatGoogleGenerativeAI:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise ValueError(
            "GOOGLE_API_KEY is not set. Open the .env file and paste your Gemini API key."
        )
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=temperature,
        google_api_key=api_key,
    )


def generate_question(topic: str) -> str:
    """Generate one interview question for the given topic."""
    model = get_model(temperature=0.8)
    response = model.invoke(
        [HumanMessage(content=QUESTION_PROMPT.format(topic=topic))]
    )
    return response.content.strip()


def score_answer(question: str, answer: str) -> str:
    """Score the candidate's answer and return structured feedback."""
    model = get_model(temperature=0.2)
    response = model.invoke(
        [HumanMessage(content=SCORING_PROMPT.format(question=question, answer=answer))]
    )
    return response.content.strip()


def generate_followup_question(topic: str, exchange_history: list) -> str:
    """Generate a deeper follow-up interview question based on prior exchanges."""
    model = get_model(temperature=0.8)

    parts = []
    for i, ex in enumerate(exchange_history, 1):
        parts.append(
            f"Exchange {i}:\n"
            f"  Q: {ex['question']}\n"
            f"  A: {ex['answer']}\n"
            f"  Feedback: {ex['feedback']}"
        )
    prior_exchanges = "\n\n".join(parts) if parts else "None yet."

    response = model.invoke(
        [HumanMessage(content=FOLLOWUP_QUESTION_PROMPT.format(
            topic=topic,
            prior_exchanges=prior_exchanges,
        ))]
    )
    return response.content.strip()
