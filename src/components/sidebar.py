import streamlit as st
import os
import requests


# Sidebar Configuration

def render_sidebar():
    """Render the sidebar and handle API key & model configuration."""
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.write("")
        with st.expander("🤖 Model Selection", expanded=True):
            provider = st.radio(
                "Select LLM Provider",
                ["OpenAI", "GROQ", "Ollama"],
                help="Choose which Large Language Model provider to use",
                horizontal=True
            )
    
    if provider == "OpenAI":
        model_option = st.selectbox(
            "Select OpenAI Model",
            ["gpt-4o-mini", "gpt-4o", "o1", "o1-mini", "o1-preview", "o3-mini", "Custom"],
            index=0
        )
        if model_option == "Custom":
            model = st.text_input("Enter your custom OpenAI model:", value="", help="Specify your custom model string")
        else:
            model = model_option
    elif provider == "GROQ":
        model = st.selectbox(
            "Select GROQ Model",
            [
                "qwen-2.5-32b",
                "deepseek-r1-distill-qwen-32b",
                "deepseek-r1-distill-llama-70b",
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
                "Custom"
            ],
            index=0,
            help="Choose from GROQ's available models. All these models support tool use and parallel tool use."
        )
        if model == "Custom":
            model = st.text_input("Enter your custom GROQ model:", value="", help="Specify your custom model string")

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