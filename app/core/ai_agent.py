from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings
from app.common.logger import get_logger

logger = get_logger(__name__)

def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):

    llm = ChatGroq(model=llm_id)
    # llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=settings.GROQ_API_KEY)/s

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    logger.info("Invoking AI agent with the provided query and settings")

    state = {"messages" : query}

    response = agent.invoke(state)

    logger.info("Received response from AI agent")

    messages = response.get("messages")

    logger.info(f"Extracted {len(messages)} messages from the agent's response")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]