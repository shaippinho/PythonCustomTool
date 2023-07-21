from langchain.agents import initialize_agent, AgentType, load_tools
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
from langchain.chat_models import AzureChatOpenAI
from customTool import search_api
import json
import os
OPENAI_API_TYPE = "Azure"
OPENAI_API_VERSION = "2023-06-01-preview"
OPENAI_API_BASE = "https://xxx.openai.azure.com"
OPENAI_API_KEY = "cxxxf27240d0xxxf904fxxxa1e38exxx"
DEPLOYMENT_NAME = "gpt-35-turbo"


# import custom tools


chat = AzureChatOpenAI(
    openai_api_base=OPENAI_API_BASE,
    openai_api_version=OPENAI_API_VERSION,
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type=OPENAI_API_TYPE,
    verbose=True
)

tools = load_tools(["llm-math"], llm=chat)
tools.append(search_api)
# tools = [
#    search_api
# ]
agent = initialize_agent(
    tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

with get_openai_callback() as cb:
    response = agent.run("Multiplique a idade de Deus por 2.")
    print('response', response)
    print(f"Total tokens {cb.total_tokens}")
    print(f"Prompt tokens {cb.prompt_tokens}")
    print(f"Completions tokens {cb.completion_tokens}")
    print(f"Total Cost {cb.total_cost}")
