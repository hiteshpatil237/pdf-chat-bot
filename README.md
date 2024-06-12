# PDF Chatbot Application

Welcome to the PDF Chatbot Application! This project leverages advanced Natural Language Processing (NLP) techniques to enable users to interact with PDF documents using natural language queries. By combining Streamlit, OpenAI, and FAISS, we have created an intuitive and efficient system for querying and retrieving information from PDFs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Live Demo](#live-demo)

## Introduction

The PDF Chatbot Application extracts text from PDF documents, splits the text into manageable chunks, generates embeddings using OpenAI's models, and stores these embeddings in a FAISS vector store. Users can then interact with the PDFs by asking questions in natural language, and the application retrieves the most relevant information based on the embeddings.

## Features

- **PDF Text Extraction:** Extracts text from uploaded PDF documents.
- **Text Chunking:** Splits extracted text into chunks for efficient processing.
- **Embeddings Generation:** Utilizes OpenAI models to generate embeddings for text chunks.
- **Vector Store:** Stores embeddings in a FAISS vector store for efficient similarity search.
- **Conversational Interface:** Provides a conversational interface for querying PDF content.
- **Advanced Prompt Engineering:** Utilizes techniques like Self-Refine and Chain-of-Thought for optimized model outputs.

## Installation

To set up the application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hiteshpatil237/pdf-chat-bot.git
   cd pdf-chat-bot

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

3. **Set up environment variables:**
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'

## Usage

1. **Run Application:**
   ```bash
   streamlit run main.py

## Technologies Used

1. **LangChain**: Framework for natural language and SQL integration.
2. **OpenAI**: Large language models for natural language understanding and generation.
3. **HuggingFace Sentence Transformers** Sentence Transformer: For generating embeddings.
4. **FAISS**: For efficient similarity searches in vector databases.
5. **Python**: Programming language for building the application.

## Live Demo

**This app is hosted on**: pdf-data-analyzer.streamlit.app
