# Chat with GitHub Repository 💬

This project allows you to interact with a GitHub repository using a chatbot interface. You can ask questions related to a specific GitHub repo, and the chatbot will answer using embeddings from the code and documentation present in the repository.

Two versions of the app are provided, one using **Ollama with Llama-3** for the chatbot's LLM (Large Language Model) and embedding, and another using **OpenAI API**. The project uses **Streamlit** for the user interface, **EmbedChain** for handling the repository data, and **GithubLoader** to load repositories into the knowledge base.

## Features:
- Chat with any GitHub repository.
- View answers based on the repo's documentation and code.
- Customizable backend with OpenAI or Ollama for natural language processing.
- Add repositories to a knowledge base for improved interaction.
- State management via Streamlit's session state to preserve user interactions.

---

## Prerequisites:
Before running the app, make sure you have the following installed:

- Python 3.7 or higher
- Streamlit
- EmbedChain
- Github API Token
- OpenAI API Key (optional for the OpenAI version)

### Install required dependencies:

```bash
pip install streamlit embedchain
```

To install the Ollama SDK (for the Llama-3 model), follow the installation instructions provided on their website.

---

## Setup and Configuration

### 1. **GitHub Token**:
You'll need a GitHub personal access token to interact with the GitHub repositories. You can generate one [here](https://github.com/settings/tokens). Ensure the token has appropriate read access to the repositories you wish to interact with.

Set the `GITHUB_TOKEN` as an environment variable:

```bash
export GITHUB_TOKEN="your-github-token"
```

### 2. **OpenAI Token (for OpenAI version)**:
If you plan to use the OpenAI version, you'll need to provide your **OpenAI API key**. Set it as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

---

## Usage

### chat_github_llama3.py: **Run with Ollama and Llama-3 Model**

This version uses the **Llama-3** model running with **Ollama** for natural language processing. It also includes database management with **Chroma**.

#### Steps:
1. The app loads a GitHub repository by adding it to the knowledge base using the `GithubLoader`.
2. After the repository is added, you can ask the bot questions related to the repository.
3. The app interacts with **Llama-3**, hosted on a local server, to generate answers.

#### Key Features of this Version:
- The `embedchain_bot()` function configures the backend with **Ollama**'s Llama-3 model.
- Temporary **Chroma** databases are used to manage embeddings.
- The app uses **Streamlit session state** for persistence across interactions.

---

### chat_github.py: **Run with OpenAI API**

This version uses **OpenAI API** for answering questions, without a custom Llama model.

#### Steps:
1. The app loads a GitHub repository into the knowledge base using the `GithubLoader`.
2. The user provides an **OpenAI API key** for natural language processing.

#### Key Features of this Version:
- Uses **OpenAI's API** for generating responses.
- Simpler configuration (no Llama-3 model).
- The app doesn't use Chroma for database management; it relies on the GitHub loader only.

---

## Streamlit UI

Both versions of the app provide a simple and interactive Streamlit UI:

1. **GitHub Repository Input**: Users input the GitHub repository URL they want to query.
2. **Prompt Input**: Users can type any question related to the repository.
3. **Answer Display**: The bot will display answers based on the data from the repository.

---

## Code Explanation

### First Code (Ollama + Llama-3 version):
- **`get_loader()`**: Sets up the `GithubLoader` with the GitHub token.
- **`embedchain_bot()`**: Initializes the EmbedChain app with Llama-3 model configuration and Chroma DB for storage.
- **`make_db_path()`**: Creates a temporary directory to store embeddings in a Chroma database.
- **State Management**: Uses `st.session_state` to manage the loader, app, and repositories across Streamlit sessions.
- **Model Setup**: Configures Llama-3 through **Ollama** for both embedding and LLM tasks.

### Second Code (OpenAI version):
- **`GithubLoader`**: Used to load the GitHub repository into the knowledge base.
- **OpenAI API Key**: Required to interact with OpenAI’s API for generating responses.
- **Streamlit UI**: A simpler setup, no custom model or Chroma database, just direct interaction with the OpenAI API.

---

