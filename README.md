# 🔍 AI Research Assistant [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://airesearch-assistant.streamlit.app/)

A powerful research assistant built with CrewAI, Exa, and Streamlit that helps you research any topic using AI Agents.

![App Screenshot](app.png)

## 🌟 Features

- 🤖 Multiple LLM Support
- 🔍 Advanced answering capabilities using Exa
- 📊 Real-time research process visualization
- 📝 Structured research reports
- 🎯 Topic-focused research and analysis
- 🔒 Secure API key management
- 📱 Responsive and modern UI

## 📚 Code Organization

- **Main Application (`app.py`)**:
  - Configures the Streamlit interface
  - Manages the research workflow
  - Handles result display

- **Research Component (`researcher.py`)**:
  - Configures LLM providers (OpenAI, GROQ, Ollama)
  - Creates research agents with appropriate tools
  - Defines research task structure
  - Manages the research execution process

- **Sidebar Component (`sidebar.py`)**:
  - Handles model selection UI
  - Manages API key input
  - Integrates with local Ollama instance
  - Provides configuration options

- **Output Handler (`output_handler.py`)**:
  - Captures and formats research process output
  - Manages real-time display updates


## 🛠️ Project Structure

```
Ai-Research-Assistant/
├── app.py # Main Streamlit application entry point
├── requirements.txt # Project dependencies
└── src/
├── components/
│ ├── researcher.py # Research agent and task implementation
│ │ # - LLM configuration
│ │ # - Research task creation
│ │ # - Exa search integration
│ └── sidebar.py # Sidebar UI and configuration
│ # - Model selection
│ # - API key management
│ # - Ollama integration
└── utils/
└── output_handler.py # Process output management
   # - Real-time output capture
   # - Output formatting
```

## 📋 Requirements

- Python >=3.10 and <3.13
- OpenAI API key or GROQ API key
- Exa API key
- Streamlit

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/hardikjp7/Ai-Research-Assistant.git
cd Ai-Research-Assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## 🔑 API Keys Setup

The application requires the following API keys:

1. **OpenAI API Key** or **GROQ API Key**
   - For OpenAI: Get it from [OpenAI Platform](https://platform.openai.com/)
   - For GROQ: Get it from [GROQ Console](https://console.groq.com/)

2. **Exa API Key**
   - Get it from [Exa](https://exa.ai)

Enter these keys in the sidebar of the application when prompted.

## 🎯 Usage

1. Open the application in your web browser
2. Select your preferred LLM provider (OpenAI or GROQ)
3. Enter your API keys in the sidebar
4. Type your research query in the text area
5. Click "Start Research" to begin the research process
6. View the real-time research process and final results

## 💡 Features in Detail

### Research Agent
The research agent (`src/components/researcher.py`) is powered by CrewAI and configured to:
- Conduct thorough research on given topics
- Analyze and summarize information
- Provide structured reports with key findings

### Process Output
The output handler (`src/utils/output_handler.py`) provides:
- Real-time process visualization
- Clean, formatted output
- Progress tracking

### User Interface
The application features a modern, responsive UI with:
- Intuitive sidebar configuration
- Clear process visualization
- Organized research results
- Professional styling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Made with ❤️ by Hardik
