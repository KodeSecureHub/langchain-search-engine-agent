# 🔎 LangChain Search Engine Agent

An AI-powered **Search Engine Agent** built using **Streamlit, LangChain, Groq, DuckDuckGo, Wikipedia, and ArXiv**.

The application allows users to ask questions and lets the LangChain agent choose the appropriate tool to search the web, Wikipedia, or academic research papers.

## Features

* Interactive Streamlit web interface
* LangChain AI agent
* Groq LLM integration
* DuckDuckGo web search
* Wikipedia search
* ArXiv research paper search
* Automatic tool selection
* Chat history
* Secure Groq API key input
* Simple and user-friendly interface

## Technologies Used

* **Python**
* **Streamlit**
* **LangChain**
* **Groq**
* **DuckDuckGo**
* **Wikipedia**
* **ArXiv**
* **python-dotenv**

## Groq Model

The application uses the following Groq model:

* `openai/gpt-oss-120b`

> Model availability may depend on the Groq API and your account/API access.

## Project Structure

```text
langchain-search-engine-agent/
│
├── app.py
├── tools_agents.ipynb
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```

## How It Works

The application follows this basic flow:

```text
User Question
      ↓
Streamlit Interface
      ↓
LangChain Agent
      ↓
Groq LLM
      ↓
 ┌────┼─────────────┐
 ↓    ↓             ↓
Web  Wikipedia    ArXiv
Search              Search
 ↓    ↓             ↓
 └────┼─────────────┘
      ↓
 Final Answer
```

The agent selects the appropriate tool based on the user's question.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/langchain-search-engine-agent.git
```

Move into the project directory:

```bash
cd langchain-search-engine-agent
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If DuckDuckGo gives a missing package error:

```bash
pip install -U ddgs
```

### 4. Configure API Keys

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

You can also enter your Groq API key directly through the application's sidebar.

**Never commit API keys or other secrets to GitHub.**

## Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## Tools

### DuckDuckGo

Used for general web searches and current information.

### Wikipedia

Used for general factual information and background knowledge.

### ArXiv

Used for searching academic research papers.

### Groq

Provides the large language model used by the LangChain agent.

## Example Questions

### General Information

```text
What is machine learning?
```

### Web Search

```text
What are the latest developments in Generative AI?
```

### Wikipedia

```text
Who is Alan Turing?
```

### Research Papers

```text
Find research papers about Retrieval Augmented Generation.
```

```text
Find research papers about Large Language Models.
```

## Requirements

Example `requirements.txt`:

```text
streamlit
langchain
langchain-community
langchain-groq
arxiv
wikipedia
ddgs
python-dotenv
```

## Security

API keys should never be hardcoded in the source code or committed to GitHub.

The `.gitignore` file excludes:

```text
.env
venv/
__pycache__/
```

If an API key is accidentally pushed to GitHub, **revoke or rotate the key immediately**.

## Future Improvements

* Add conversation memory
* Add source citations
* Add more search tools
* Add PDF document search
* Add RAG functionality
* Add streaming responses
* Improve UI
* Deploy the application online

## Learning Outcomes

Through this project, I practiced:

* Building AI applications with Streamlit
* Creating LangChain agents
* Integrating Groq LLMs
* Using LangChain tools
* Web search integration
* Wikipedia integration
* ArXiv integration
* Managing API keys securely
* Working with environment variables
* Building AI-powered search applications

## Author

**Kodeeswaran A S**

B.Tech – Computer Science and Business Systems

Interested in **AI/ML, Generative AI, Software Development, and Cybersecurity**.

---

⭐ If you find this project useful, consider giving the repository a star!
