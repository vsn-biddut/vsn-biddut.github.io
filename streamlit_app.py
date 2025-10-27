import streamlit as st
import streamlit.components.v1 as components

# Page configuration (fullscreen, no menu)
st.set_page_config(
    page_title="",
    page_icon="",
    layout="wide",      # Full width
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header/footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
body {margin:0; padding:0;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Embed HTML full screen
components.html(html_content, height=2000, scrolling=False)



