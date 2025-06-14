import streamlit as st
import os
import requests


# Sidebar Configuration

def render_sidebar():
    """Render the sidebar and handle API key & model configuration."""
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.write("")
        
        # Basic provider selection
        provider = st.radio(
            "Select LLM Provider",
            ["OpenAI", "GROQ"],
            help="Choose which Large Language Model provider to use",
            horizontal=True
        )
        
    return {
        "provider": provider,
        "model": None
    }