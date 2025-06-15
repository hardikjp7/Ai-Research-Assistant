try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except (ImportError, KeyError):
    pass

import streamlit as st
import os
from src.components.sidebar import render_sidebar

# Configure the page
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🔍 :red[AI] Research Assistant", anchor=False)

# Render sidebar and get selection (provider and model)
selection = render_sidebar()

# Basic input section
input_col1, input_col2, input_col3 = st.columns([1, 3, 1])
with input_col2:
    task_description = st.text_area(
        "What would you like to research?",
        value="Research the latest AI Agent news in February 2025 and summarize each.",
        height=68
    )

# Start button
col1, col2, col3 = st.columns([1, 0.5, 1])
with col2:
    start_research = st.button("🚀 Start Research", use_container_width=False, type="primary")

if start_research:
    st.info(f"Selected provider: {selection['provider']}, Model: {selection['model']}")
    st.info("Research functionality will be implemented soon...")