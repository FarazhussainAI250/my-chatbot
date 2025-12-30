# chatbot_app.py

import streamlit as st

# ---------------------------
# Knowledge Base
# ---------------------------
qa_data = {
    "name": "My name is Faraz.",
    "who are you": "I am Faraz, a student of FA (IT) from Pakistan.",
    "country": "I am from Pakistan.",
    "language": "I prefer Urdu / Roman Urdu with a little English.",
    "study": "I am studying FA (IT).",
    "background": "I have a Computer / IT background.",
    "backend": "I am learning backend development.",
    "mysql": "I am currently working with MySQL.",
    "website": "I have built websites using Flask, HTML, CSS and JavaScript.",
    "dashboard": "I am working on admin panels and dashboards.",
    "ai": "I am learning AI, ML and Generative AI.",
    "projects": "I have worked on prediction models, chatbots and Streamlit apps.",
    "portfolio": "I am focused on building a strong professional portfolio.",
    "clients": "I am interested in real-world projects and client work.",
    "communication": "I prefer professional, simple and clear communication."
}

# ---------------------------
# Response Function
# ---------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    for key in qa_data:
        if key in user_input:
            return qa_data[key]

    return "Sorry, I can only answer questions related to my profile."

# ---------------------------
# UI
# ---------------------------
st.set_page_config(page_title="Faraz Assistant 🤖", page_icon="🤖")
st.title("🤖 Faraz Personal Assistant")
st.write("Ask me questions related to my profile")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- Form (IMPORTANT FIX) ----
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question")
    submit = st.form_submit_button("Send")

if submit and user_input:
    answer = chatbot_response(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# Display chat
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")

