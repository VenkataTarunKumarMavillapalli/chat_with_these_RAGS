# Chat with Your Gmail Inbox 📧

This project enables users to interact with their Gmail inbox through a chatbot interface, powered by the **OpenAI GPT-4 Turbo** model. Using **EmbedChain** and **Chroma** for embedding and managing the email data, this application allows you to query your Gmail inbox and get responses based on the content of your emails.

With **Streamlit** for the user interface, the app can pull emails from your inbox, add them to a knowledge base, and answer questions based on the contents of those emails.

---

## Features:
- **Chat with Your Gmail Inbox**: Ask questions about the emails you’ve received in your Gmail inbox.
- **OpenAI GPT-4 Turbo Integration**: Uses OpenAI’s GPT-4 Turbo for natural language processing and generating answers.
- **EmbedChain Backend**: Utilizes **EmbedChain** for managing the repository of emails and embeddings.
- **Chroma Database**: Embedding and knowledge base storage powered by **Chroma**.
- **Secure Integration**: Input your OpenAI API key securely for interaction with the OpenAI API.

---

## Prerequisites:
Before running the app, ensure you have the following:

- **Python 3.7 or higher**.
- **Streamlit**: For the front-end interface.
- **EmbedChain**: For managing the knowledge base.
- **OpenAI API Key**: To power the chatbot with GPT-4 Turbo.
- **Google Gmail API Setup**: You need to set up Gmail API access to allow the app to fetch your emails.

### Install the required dependencies:

To install the dependencies, run the following:

```bash
pip install streamlit embedchain openai chromadb
```

### Gmail API Setup:
To interact with your Gmail inbox, you will need to enable Gmail API access:

1. Visit the [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project or use an existing one.
3. Enable the **Gmail API** for your project.
4. Create credentials for your application (OAuth2.0 or API keys).
5. Download the credentials file (usually a `.json` file).
6. For this app, you may need to use Gmail's **label filtering** (e.g., `to: me label:inbox`) to get messages from your inbox.

---

## Setup and Configuration:

### 1. **Obtain OpenAI API Key:**
Sign up or log in to OpenAI and generate an API key for accessing **GPT-4 Turbo**.

### 2. **Set Up Your Gmail Access:**
Ensure you have your **Gmail API credentials** file set up correctly. You will need this to fetch the emails and process them in the app.

### 3. **Run the Streamlit App:**

Once the required dependencies and setup are complete, you can run the app as follows:

```bash
streamlit run app.py
```

This will launch the Streamlit interface in your browser.

### 4. **Enter OpenAI API Key:**
Once the app is running, you will be prompted to input your **OpenAI API key** via a secure input field.

### 5. **Fetch Gmail Inbox Data:**
After entering the OpenAI API key, the app will automatically fetch emails from your Gmail inbox using the **Gmail API**. The emails are filtered based on the **Gmail filter** you provide in the code (e.g., `to: me label:inbox`).

### 6. **Ask Questions:**
You can now interact with your inbox. Type in any question related to your emails in the input box, and the chatbot will return relevant information based on the emails stored in the knowledge base.

---

## Code Explanation:

### `embedchain_bot(db_path, api_key)`:
This function initializes the **EmbedChain App** with the configuration for:
- **LLM**: OpenAI GPT-4 Turbo model for processing questions and answers.
- **Embedding**: Uses OpenAI for embedding the email content into a knowledge base.
- **Vector Database**: Chroma is used as the backend to store email embeddings.

### **Streamlit App UI**:
- The **OpenAI API Key** is securely entered by the user through the Streamlit interface.
- A temporary database directory is created using **`tempfile.mkdtemp()`**.
- The **Gmail Filter** is statically set to `to: me label:inbox`, which pulls emails from the inbox. You can modify the filter to suit different labels or email categories if needed.
- The **Gmail Data** is added to the knowledge base using the `app.add()` method.
- **Query Processing**: The user can input any question, and the app will query the knowledge base to return an appropriate answer using `app.query()`.

---

## Example Interaction:

1. Launch the app: `streamlit run app.py`
2. Input your **OpenAI API key**.
3. Wait for the app to process your Gmail inbox data.
4. Ask questions such as:
   - "What is the subject of the latest email?"
   - "Can you summarize the email from John Doe?"
   - "What are the key points in the email about the meeting?"

---

## Future Enhancements:

- **Email Filtering**: Improve filtering capabilities (e.g., by specific sender, date range, or label).
- **Gmail OAuth Authentication**: Implement a more secure OAuth-based Gmail authentication to directly access emails without needing to set the filter statically.
- **Multi-language Support**: Add support for multi-language queries and responses.
- **Improve Knowledge Base Storage**: Use persistent storage options or cloud databases for better scalability.


