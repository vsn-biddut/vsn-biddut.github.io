import streamlit as st

st.set_page_config(page_title="HTML Preview", layout="wide")

st.title("🌐 My HTML Page")

# index.html ফাইল ওপেন করে Streamlit এর মধ্যে দেখানো
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)


