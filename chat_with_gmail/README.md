# Chat with Your Gmail Inbox 📧

This project is a **Streamlit-based app** that allows users to interact with their Gmail inbox using OpenAI's GPT models. By fetching emails from Gmail and adding them to a knowledge base, users can ask questions about their emails and get intelligent responses.

---

## Features
- **Authenticate with Gmail:** Securely connect to your Gmail account using OAuth2 authentication.
- **Fetch Emails:** Retrieve email snippets from your inbox with customizable filters.
- **Chat with Emails:** Use OpenAI's GPT model to ask questions about the fetched emails.
- **Interactive UI:** Built with Streamlit for an intuitive user experience.

---

## Prerequisites

### 1. **Set up Gmail API**
To access your Gmail data, you'll need to set up the Gmail API:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Enable the **Gmail API** under **APIs & Services > Library**.
4. Create **OAuth 2.0 Client ID** credentials:
   - Navigate to **APIs & Services > Credentials**.
   - Configure the consent screen (provide app name, email, etc.).
   - Download the `credentials.json` file.
5. Place the `credentials.json` file in the project directory.

### 2. **OpenAI API Key**
Sign up for OpenAI and get your API key from [OpenAI's platform](https://platform.openai.com/).

---

## Usage

### Step 1: Run the App
```bash
streamlit run app.py
```

### Step 2: Authenticate Gmail
1. When prompted, authenticate your Gmail account via the web browser.
2. Consent to the requested permissions.
3. A `token.json` file will be generated for future use.

### Step 3: Enter OpenAI API Key
1. Provide your OpenAI API key in the text field.
2. This key will be used to query the GPT model.

### Step 4: Fetch and Query Emails
1. Click the **"Fetch and Add Emails"** button to load emails from your inbox into the knowledge base.
2. Use the text input to ask questions about your emails.

---

## Project Structure
```plaintext
.
├── app.py                # Main Streamlit app file
├── credentials.json      # Gmail API credentials (required)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
├── token.json            # Gmail authentication token (auto-generated)
```

---

## Configuration

### Gmail Query Filters
By default, the app uses the query `label:inbox` to fetch emails. You can modify this query in the `fetch_emails` function:
```python
fetch_emails(service, query="label:inbox", max_results=10)
```
For example, to fetch unread emails:
```python
fetch_emails(service, query="label:unread", max_results=10)
```

---

## Dependencies

Install all dependencies using the `requirements.txt` file:
```plaintext
streamlit
embedchain
google-auth
google-auth-oauthlib
google-api-python-client
```

---

## Security
1. Never expose your `credentials.json` or `token.json` files publicly (e.g., in GitHub repositories).
2. Use environment variables or secret managers for sensitive data like the OpenAI API key.

---

## Troubleshooting

### Gmail Authentication Issues
- Ensure the `credentials.json` file is valid and located in the correct directory.
- Delete the `token.json` file and re-authenticate if needed.

### OpenAI API Errors
- Verify that your OpenAI API key is valid and has enough usage quota.

### Missing Emails
- Modify the Gmail query filter in the `fetch_emails` function to match your requirements.

---

## Acknowledgments
- [Streamlit](https://streamlit.io/) for creating an amazing framework for building data-driven apps.
- [Google API Client](https://developers.google.com/api-client-library/python) for enabling seamless Gmail integration.
- [OpenAI](https://openai.com/) for providing the GPT models.

---

## Contact
For any questions or feedback, feel free to reach out:
- [**LinkedIn**](https://www.linkedin.com/in/venkata-tarun-kumar-mavillapalli-967b4613a/)


