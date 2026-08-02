import streamlit as st

from agent import generate_followup_question, generate_question, score_answer

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Interview Practice Bot",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Interview Practice Bot")

TOPICS = ["Python", "GenAI Fundamentals", "RAG", "AI Agents"]


# ── Session helpers ─────────────────────────────────────────────────────────────
def reset_session(topic: str) -> None:
    """Generate a new question and reset all session state."""
    with st.spinner("Generating question..."):
        try:
            question = generate_question(topic)
        except Exception as exc:
            st.error(f"Could not generate a question: {exc}")
            st.stop()

    st.session_state.topic = topic
    st.session_state.current_question = question
    st.session_state.chat_history = [{"role": "assistant", "content": question}]
    st.session_state.awaiting_answer = True
    st.session_state.user_answer = ""
    st.session_state.feedback = ""
    st.session_state.exchange_history = []
    # Increment the lifetime question counter
    st.session_state.questions_asked = st.session_state.get("questions_asked", 0) + 1


# ── Sidebar ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    topic = st.selectbox("Topic", TOPICS)
    new_q = st.button("🔄 New Question")

    st.divider()
    st.markdown("### Session Info")
    if "topic" in st.session_state:
        st.markdown(f"**Topic:** {st.session_state.topic}")
        st.markdown(f"**Questions asked:** {st.session_state.get('questions_asked', 0)}")
        followups = len(st.session_state.get("exchange_history", []))
        status = "Waiting for answer" if st.session_state.awaiting_answer else "Review feedback"
        st.markdown(f"**Status:** {status}")
        if followups:
            st.markdown(f"**Follow-ups done:** {followups}")


# ── Initialize or reset session ─────────────────────────────────────────────────
if "topic" not in st.session_state:
    # First load
    reset_session(topic)
elif new_q or st.session_state.topic != topic:
    # New question button clicked, or topic changed
    reset_session(topic)


# ── Render chat history ─────────────────────────────────────────────────────────
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ── Follow-up button (visible only after an answer has been scored) ──────────────
if not st.session_state.awaiting_answer and st.session_state.get("feedback"):
    if st.button("🔁 Ask Follow-up Question"):
        # Save the completed exchange before generating the next question
        st.session_state.exchange_history.append({
            "question": st.session_state.current_question,
            "answer": st.session_state.user_answer,
            "feedback": st.session_state.feedback,
        })
        with st.spinner("Generating follow-up question..."):
            try:
                followup_q = generate_followup_question(
                    st.session_state.topic,
                    st.session_state.exchange_history,
                )
            except Exception as exc:
                st.error(f"Could not generate a follow-up: {exc}")
                st.stop()
        st.session_state.current_question = followup_q
        st.session_state.chat_history.append({"role": "assistant", "content": followup_q})
        st.session_state.awaiting_answer = True
        st.session_state.user_answer = ""
        st.session_state.feedback = ""
        st.rerun()


# ── Answer input (visible only when awaiting an answer) ──────────────────────────
if st.session_state.awaiting_answer:
    if user_input := st.chat_input("Type your answer..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        try:
            with st.spinner("Evaluating your answer..."):
                response = score_answer(st.session_state.current_question, user_input)
            st.session_state.user_answer = user_input
            st.session_state.feedback = response
            st.session_state.awaiting_answer = False
        except Exception as exc:
            response = f"⚠️ Something went wrong: {exc}"
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
