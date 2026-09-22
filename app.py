import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Commercial Banking · Client Journey Architecture",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit default padding
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            background: #060912;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
            padding: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Load and render the HTML file
with open("architecture.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1100, scrolling=True)
