# Research Papers Chat Apps: OpenAI GPT-4o & Llama-3

This repository contains two applications designed to help users chat with research papers from **arXiv**. The apps leverage different AI models for query processing and retrieval:

1. **OpenAI GPT-4o - Research Papers**: Utilizes the cloud-based OpenAI GPT-4o model.
2. **Llama-3 - Research Papers**: Employs the locally running Llama-3 model for offline use.

Each app is built with **Streamlit**, providing an intuitive interface for querying research papers.

---

## Features
- **User-Friendly Interface**: Simple and clean interface for interacting with AI-powered research tools.
- **ArXiv Integration**: Search and chat about research papers directly from the arXiv database.
- **AI-Driven Assistance**: Provides intelligent responses to research-related queries.
- **Two Deployment Options**:
  - Cloud-based using OpenAI GPT-4o.
  - Local deployment using Llama-3 for enhanced privacy.

---

## Prerequisites
Before running either app, ensure you have the following:

### Common Requirements
- **Python**: Version 3.9 or higher.
- **Streamlit**: Install using `pip install streamlit`.
- **Phi Library**: Install using `pip install phi`.

### OpenAI GPT-4o - Research Papers (Code 1)
- **OpenAI API Key**: An active OpenAI account and API key are required to use GPT-4o.
- **Internet Connection**: The app communicates with OpenAI’s cloud servers.

### Llama-3 - Research Papers (Code 2)
- **Llama-3 Model**: A locally running instance of the Llama-3 model. You can use [Ollama](https://ollama.ai/) to set up the model.
- **Local Resources**: Ensure sufficient computational resources for running Llama-3 locally (e.g., GPU or high-performance CPU).

---

## Running the Apps
You can choose to run either the **OpenAI GPT-4o - Research Papers** app or the **Llama-3 - Research Papers** app:

### 1. OpenAI GPT-4o - Research Papers
#### User Workflow:
1. Enter your OpenAI API Key in the provided input field.
2. Enter your search query in the text box (e.g., "quantum computing advancements").
3. View the assistant's response containing information about relevant research papers.

### 2. Llama-3 - Research Papers
#### User Workflow:
1. Ensure the Llama-3 model is running locally before starting the app.
2. Enter your search query in the text box (e.g., "machine learning in healthcare").
3. View the assistant's response containing insights and relevant research papers.

---

## Customization
- **Temperature Settings (Code 1)**: Adjust `temperature` in the `OpenAIChat` initialization to control response creativity.
- **Tool Debugging (Code 2)**: Set `show_tool_calls=False` in the `Assistant` initialization to hide tool debugging outputs.
- **Model Changes**:
  - For **OpenAI GPT-4o**, modify the model type (e.g., "gpt-3.5-turbo").
  - For **Llama-3**, update the model name (e.g., "llama3:chat").

---

## Known Issues
1. **OpenAI GPT-4o**:
   - API key misconfiguration may result in authentication errors.
   - Requires an active internet connection.
2. **Llama-3**:
   - Model performance depends on available hardware resources.
   - Debugging local setups may require familiarity with machine learning frameworks.

---

## Contact
For any questions or feedback, feel free to reach out:
- [**LinkedIn**](https://www.linkedin.com/in/venkata-tarun-kumar-mavillapalli-967b4613a/)

