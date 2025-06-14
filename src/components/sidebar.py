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

        with st.expander("🔑 API Keys", expanded=True):
            st.info("API keys are stored temporarily in memory and cleared when you close the browser.")
            if provider == "OpenAI":
                openai_api_key = st.text_input(
                    "OpenAI API Key",
                    type="password",
                    placeholder="Enter your OpenAI API key",
                    help="Enter your OpenAI API key"
                )
                if openai_api_key:
                    os.environ["OPENAI_API_KEY"] = openai_api_key
            elif provider == "GROQ":
                groq_api_key = st.text_input(
                    "GROQ API Key",
                    type="password",
                    placeholder="Enter your GROQ API key",
                    help="Enter your GROQ API key"
                )
                if groq_api_key:
                    os.environ["GROQ_API_KEY"] = groq_api_key
            
            # EXA API key for web search
            exa_api_key = st.text_input(
                "EXA API Key",
                type="password",
                placeholder="Enter your EXA API key",
                help="Enter your EXA API key for web search capabilities"
            )
            if exa_api_key:
                os.environ["EXA_API_KEY"] = exa_api_key

    return {
        "provider": provider,
        "model": None
    }