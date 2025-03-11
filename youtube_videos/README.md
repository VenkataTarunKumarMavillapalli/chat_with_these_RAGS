# YouTube Video Chat with OpenAI API

This Streamlit app allows users to interact with YouTube videos using OpenAI's GPT-4 model. By extracting the transcript of a YouTube video, the app enables users to ask questions and receive answers based on the video's content.

---

## Features

- **Interact with YouTube Videos**: Ask questions about any YouTube video and receive detailed answers.
- **Transcripts from YouTube**: Automatically fetches transcripts from YouTube videos.
- **Customizable OpenAI GPT-4 Integration**: Allows users to connect their own OpenAI API key to use GPT-4 for generating answers.
- **Embedding Knowledge Base**: Uses EmbedChain and Chroma to store and query video transcripts.

---

## Requirements

Before running the app, ensure you have the following dependencies installed:

- Python 3.7 or higher
- Streamlit: Web framework to build the app
- OpenAI: GPT API for generating responses
- EmbedChain: A framework to embed text and chat with the model
- YouTube Transcript API: Extract transcripts from YouTube videos
- Chroma: Vector database for storing video embeddings

---

### 3. Interact with YouTube Videos

1. **Enter your OpenAI API key** in the provided input field.
2. **Enter a YouTube video URL** in the second input field.
   - The app supports both regular YouTube videos and YouTube Shorts URLs.
3. **Chat with the video**: After the transcript is fetched, you can ask any question about the video, and the model will provide an answer based on the transcript.

---

## Code Overview

### `chat_youtube.py`

- **Imports**: Imports necessary libraries such as `streamlit`, `embedchain`, `openai`, and `youtube_transcript_api`.
- **embedchain_bot(db_path: str, api_key: str)**: Initializes and returns an instance of EmbedChain with a specific configuration.
- **extract_video_id(video_url: str)**: Extracts the video ID from a provided YouTube URL (works with both normal videos and Shorts).
- **fetch_video_data(video_url: str)**: Fetches the transcript for the provided YouTube video and returns it as text.
- **Streamlit UI**: Provides inputs for OpenAI API key and YouTube video URL, handles displaying the responses, and manages errors.
- **Temporary Database**: Creates a temporary directory for storing the video transcript using the `tempfile.mkdtemp()` method.

### Libraries

- **Streamlit**: Used to create the interactive web interface for the app.
- **EmbedChain**: Manages embeddings and stores the video transcripts for querying.
- **YouTube Transcript API**: Extracts text from video transcripts, which is used as the knowledge base for the app.
- **Chroma**: Stores embeddings to allow for querying against the stored video transcript.

---

### Streamlit UI:

- Title and description at the top, explaining the app's functionality.
- An input field for the OpenAI API key to connect the app with OpenAI services.
- If the API key is provided, it initializes the Embedchain app and sets up the temporary vector database.
- A text input for the YouTube video URL, where the app will fetch the video’s transcript and store it in the knowledge base.
- Once the video is added, the user can type in any question related to the video, and the app will use OpenAI to generate a response.

---

## Troubleshooting

- **API Key Issue**: If the OpenAI API key is invalid or missing, the app will not work. Make sure the API key is correct and active.
- **No Transcript Available**: If a video doesn't have an available transcript, the app will display a warning and will not allow the user to ask questions about the video.
- **Video URL**: Ensure the URL provided is a valid YouTube link (either regular or Shorts). Invalid URLs will raise an error.

---

## Potential Improvements

- **Fetch Video Title**: The app currently uses "Unknown" as the title for all videos. We can enhance it to fetch the actual title from YouTube using the YouTube Data API.
- **Persistent Storage**: Currently, the vector database is stored temporarily. You may want to implement a more persistent solution for saving data across sessions.
- **Error Handling**: Additional error handling can be added to ensure smoother user experiences.

---

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests. You can help with bug fixes, documentation improvements, or new feature additions.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Acknowledgments

- **OpenAI**: For providing the GPT-4 model to interact with the YouTube video data.
- **EmbedChain**: For offering an easy-to-use framework to manage embeddings and knowledge bases.
- **YouTube Transcript API**: For providing a reliable way to fetch transcripts from YouTube videos.

---
## Contact
For any questions or feedback, feel free to reach out:
- [**LinkedIn**](https://www.linkedin.com/in/venkata-tarun-kumar-mavillapalli-967b4613a/)
