import streamlit as st

st.set_page_config(page_title="My Streamlit App", layout="centered")

st.title("🚀 Welcome to My Streamlit App")
st.write("Hello! This is a test deployment from Streamlit Cloud.")

name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}!")

