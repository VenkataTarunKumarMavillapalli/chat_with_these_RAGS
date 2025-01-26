# **Chat with PDF: A Streamlit Application**
This repository provides three distinct implementations of a Streamlit-based application that allows users to upload a PDF file and interact with its contents through a conversational interface. Each implementation highlights different features, backend integrations, and user experience designs.

---

## **Features**
1. **Upload PDF**: Users can upload PDF documents to extract knowledge.
2. **Chat Interface**: Users can ask questions about the uploaded PDF and receive responses.
3. **Flexible Backends**:
   - OpenAI API (**PDF - OpenAI**)
   - Local LLM (Llama models via Ollama: **PDF - Ollama (llama3.2)** and **PDF - Ollama (llama3:instruct)**).
4. **Enhanced Interactivity**:
   - **PDF Preview** and **Chat History** in **PDF - Ollama (llama3.2)**.

---

## **Installation**

### **Pre-requisites**
- Python 3.8 or later.
- A local LLM setup for **PDF - Ollama (llama3.2)** and **PDF - Ollama (llama3:instruct)**:
  - [Ollama](https://ollama.com/) must be installed and running.
  - Ensure Ollama is accessible at `http://localhost:11434`.

### **Required Python Libraries**
Install the dependencies using the following command:
```bash
pip install streamlit embedchain chromadb base64 streamlit-chat
```

---

## **Usage**

### **PDF - OpenAI**
- Enter your OpenAI API Key in the provided field.
- Upload a PDF file.
- Ask questions about the document in the text input field.
- **Features**:
  - Simple, minimal UI.
  - Dynamically accepts API key input for flexibility.

### **PDF - Ollama (llama3.2)**
- Upload a PDF file through the sidebar.
- Preview the document in the embedded viewer.
- Add the file to the knowledge base.
- Interact with the document via the chat input.
- **Features**:
  - Chat history with the ability to clear.
  - PDF preview in an embedded viewer.
  - Local Llama 3.2 model for fast, private processing.

### **PDF - Ollama (llama3:instruct)**
- Upload a PDF file and add it to the knowledge base.
- Ask questions about the document.
- **Features**:
  - Lightweight design for quick setup and usage.
  - Local Llama3 backend for embeddings and chat.

---

## **Feature Comparison**

| Feature                          | PDF - OpenAI               | PDF - Ollama (llama3.2)                 | PDF - Ollama (llama3:instruct) |
|----------------------------------|----------------------------|-----------------------------------------|--------------------------------|
| Backend LLM                      | OpenAI                     | Ollama (llama3.2)                       | Ollama (llama3:instruct)       |
| API Key Input                    | Yes                        | No                                      | No                             |
| Chat History                     | No                         | Yes                                     | No                             |
| PDF Preview                      | No                         | Yes (via iframe)                        | No                             |
| UI Complexity                    | Minimal                    | Advanced                                | Minimal                        |
| Clear Chat Button                | No                         | Yes                                     | No                             |
| Response Streaming               | No                         | Yes                                     | No                             |

---

## **Customization**

### **For PDF - OpenAI**:
- Update the OpenAI model parameters in the `embedchain_bot` function:
  ```python
  "config": {"api_key": api_key}
  ```

### **For PDF - Ollama (llama3.2)** and **PDF - Ollama (llama3:instruct)**:
- Update the Llama model parameters in the `embedchain_bot` function:
  ```python
  "model": "llama3.2:latest"  # For PDF - Ollama (llama3.2)
  "model": "llama3:instruct"  # For PDF - Ollama (llama3:instruct)
  "base_url": "http://localhost:11434"
  ```

---

## **Known Issues**
- **PDF - Ollama (llama3.2)** and **PDF - Ollama (llama3:instruct)**:
  - Ensure that Ollama is running locally. If it’s not installed or accessible, the app will not work.
- **Large PDFs**: Handling very large PDFs may result in slower embedding and response times.
- **Streamlit Layout**: In **PDF - Ollama (llama3.2)**, long chat histories may cause visual clutter. Clearing the chat history resolves this.

---

## **Contributing**
Contributions are welcome! Feel free to open an issue or submit a pull request for:
- Bug fixes.
- Feature enhancements.
- Documentation updates.

---

## **License**
This project is licensed under the MIT License.

---

## **Acknowledgments**
- [Streamlit](https://streamlit.io) for building interactive applications.
- [Embedchain](https://github.com/embedchain/embedchain) for handling vector embeddings.
- [Ollama](https://ollama.com) for local LLM support.
- [OpenAI](https://openai.com) for API-based LLM integration.

---

## Contact
For any questions or feedback, feel free to reach out:
- [**LinkedIn**](https://www.linkedin.com/in/venkata-tarun-kumar-mavillapalli-967b4613a/)

