import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello World",
    page_icon="🏠",
)

image = Image.open('images/DataStacksIcon.png')

st.image(image, caption='DataStacks')

st.write("# Welcome to DataStacks! 🏠")

st.markdown(
    """
## Your one stop shop for risk analysis.
#### Easy as 1, 2, 3!
### 1. Get Started With Risk Analysis.
### 2. View Your Portfolio's Current Performance.
### 3. Find Optimal Portfolio Based On Risk!
"""
)