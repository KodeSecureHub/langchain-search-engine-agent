import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from langchain_community.utilities import (
    ArxivAPIWrapper,
    WikipediaAPIWrapper
)

from langchain_community.tools import (
    ArxivQueryRun,
    WikipediaQueryRun,
    DuckDuckGoSearchRun
)

from langchain_community.callbacks import StreamlitCallbackHandler


# ============================================================
# Load environment variables
# ============================================================

load_dotenv()


# ============================================================
# Streamlit Page
# ============================================================

st.set_page_config(
    page_title="LangChain Search Engine",
    page_icon="🔎"
)

st.title("🔎 LangChain - Chat with Search")

st.write(
    "Ask questions and the AI agent can search the web, "
    "Wikipedia, and ArXiv."
)


# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("Settings")

api_key = st.sidebar.text_input(
    "Enter your Groq API Key:",
    type="password"
)


# ============================================================
# Tools
# ============================================================

# ArXiv Tool
arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=200
)

arxiv = ArxivQueryRun(
    api_wrapper=arxiv_wrapper
)


# Wikipedia Tool
wikipedia_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=200
)

wiki = WikipediaQueryRun(
    api_wrapper=wikipedia_wrapper
)


# DuckDuckGo Search Tool
search = DuckDuckGoSearchRun(
    name="Search"
)


tools = [
    search,
    arxiv,
    wiki
]


# ============================================================
# Chat History
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! I'm a search assistant. "
                "I can search the web, Wikipedia, and ArXiv. "
                "How can I help you?"
            )
        }
    ]


# Display previous messages
for message in st.session_state.messages:

    st.chat_message(
        message["role"]
    ).write(
        message["content"]
    )


# ============================================================
# User Input
# ============================================================

if prompt := st.chat_input(
    "What is machine learning?"
):

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    st.chat_message("user").write(prompt)


    # ========================================================
    # Check API Key
    # ========================================================

    if not api_key:

        st.error(
            "Please enter your Groq API key in the sidebar."
        )

        st.stop()


    # ========================================================
    # Groq LLM
    # ========================================================

    llm = ChatGroq(
        groq_api_key=api_key,
        model="openai/gpt-oss-120b",
        streaming=True
    )


    # ========================================================
    # Create Agent
    # ========================================================

    search_agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are a helpful AI search assistant.\n\n"

            "You have access to three tools:\n"
            "1. Search - for general and current web information.\n"
            "2. Wikipedia - for general factual information.\n"
            "3. ArXiv - for academic research papers.\n\n"

            "Choose the appropriate tool when necessary.\n"
            "For current information, prefer web search.\n"
            "For academic papers, use ArXiv.\n"
            "For general factual information, Wikipedia may be useful.\n\n"

            "Give clear and concise answers."
        )
    )


    # ========================================================
    # Assistant Response
    # ========================================================

    with st.chat_message("assistant"):

        st_cb = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=False
        )

        result = search_agent.invoke(
            {
                "messages": st.session_state.messages
            },
            config={
                "callbacks": [st_cb]
            }
        )

        # Get final response
        response = result["messages"][-1].content


        # Save response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )


        # Display response
        st.write(response)