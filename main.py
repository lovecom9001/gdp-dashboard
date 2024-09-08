import streamlit as st

st.set_page_config(page_title="ChatGPT", page_icon=".")
st.title("ChatGPT")

if user_input : = st.chat_input("메시지를 입력해 주세요."):
    st.chat_message("user").write(f"{user_input}")
