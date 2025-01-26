import tempfile
import streamlit as st
from embedchain import App
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API Scopes
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Authenticate Gmail
def authenticate_gmail():
    """Authenticate Gmail API and return the service."""
    creds = None
    token_file = "token.json"
    try:
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    except Exception:
        pass

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)

# Fetch emails from Gmail
def fetch_emails(service, query="label:inbox", max_results=10):
    """Fetch emails from Gmail."""
    messages = []
    results = service.users().messages().list(userId="me", q=query, maxResults=max_results).execute()
    if "messages" not in results:
        return messages
    for msg in results["messages"]:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        snippet = msg_data.get("snippet", "")
        messages.append(snippet)
    return messages

# Embedchain bot
def create_embedchain_bot(db_path, openai_api_key):
    """Initialize Embedchain bot."""
    return App.from_config(
        config={
            "llm": {"provider": "openai", "config": {"model": "gpt-4-turbo", "temperature": 0.5, "api_key": openai_api_key}},
            "vectordb": {"provider": "chroma", "config": {"dir": db_path}},
            "embedder": {"provider": "openai", "config": {"api_key": openai_api_key}},
        }
    )

# Streamlit app
st.title("Chat with your Gmail Inbox 📧")

# Gmail Authentication
try:
    gmail_service = authenticate_gmail()
    st.success("Authenticated with Gmail!")
except Exception as e:
    st.error(f"Error authenticating Gmail: {e}")

# OpenAI API Key
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if openai_api_key:
    # Initialize Embedchain bot
    db_path = tempfile.mkdtemp()
    bot = create_embedchain_bot(db_path, openai_api_key)

    # Fetch and add emails
    if st.button("Fetch and Add Emails"):
        try:
            st.info("Fetching emails...")
            emails = fetch_emails(gmail_service)
            add_emails_to_embedchain(bot, emails)
            st.success("Emails added to knowledge base!")
        except Exception as e:
            st.error(f"Error fetching or adding emails: {e}")

    # Query emails
    prompt = st.text_input("Ask a question about your emails")
    if prompt:
        try:
            answer = bot.query(prompt)
            st.write(answer)
        except Exception as e:
            st.error(f"Error querying emails: {e}")
