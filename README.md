**Description**
The CCDP Support Assistant is an AI-powered chatbot application designed to assist users with queries related to the CDP program. It leverages LangChain, Groq's LLM, and Chroma for conversational retrieval and efficient document querying. The application provides a seamless interface for users to interact with the chatbot and obtain relevant information from a set of pre-processed documents.

**Features**
Conversational AI: Powered by Groq's Llama 3.1 model for natural language interactions.
Document Embedding & Retrieval: Uses HuggingFace embeddings and Chroma for document vectorization.
Streamlit Interface: A user-friendly web app for interactive conversations.
Custom Query Filtering: Detects and filters out irrelevant queries based on specific keywords.
Persistent Chat Memory: Maintains chat history for better context in conversations.

**Technologies Used**
Programming Language: Python
Frameworks: LangChain, Streamlit
Libraries:
HuggingFace
Chroma
LangChain Community Modules
NLTK
Unstructured
Environment: Localhost (using Streamlit)

**Installation**
Prerequisites
Python 3.8 or above installed on your system.
An active GROQ API Key for LLM interactions.
Poppler installed for PDF processing.

**Poppler Installation**
Poppler is required to handle PDF documents. Follow the instructions below to install Poppler on your system:

**Windows:**

Download Poppler for Windows from Poppler for Windows.
Extract the downloaded archive.
Add the bin directory (inside the extracted folder) to your system's PATH environment variable.

**Usage**
Access the application via the local Streamlit interface (usually at http://localhost:8501).
Interact with the chatbot by typing your query in the input box.
Get responses based on the embedded documents and conversational context.
Use the Clear Chat button to reset the session.
**project_root/
│
├── main.py                # Main Streamlit app
├── vectorize_documents.py # Script for document vectorization
├── config.json            # Configuration file for API keys
├── requirements.txt       # Dependencies
├── vector_db_dir/         # Directory for vectorized documents (auto-generated)
├── data/                  # Folder for input documents
├── README.md              # Project documentation**

**Notes**
Ensure that the data/ folder contains all the relevant documents for query embedding.
Check requirements.txt for any library conflicts and ensure compatibility with your Python version.

**Troubleshooting**
API Errors: Verify that your GROQ API key is active and correctly added to config.json.
Vectorization Issues: Ensure the data/ folder contains readable and supported file formats (e.g., .pdf, .txt).
Missing Modules: Run the following command if any module is missing:
**pip install <module_name>**
Poppler Not Found: Verify that Poppler is installed and added to your PATH. Check by running:
**pdftotext -v**
Name: k.Prathap
Email: prathapcm018@gmail.com
