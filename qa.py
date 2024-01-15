from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_community.llms import Ollama
llm = Ollama(model="llama2", temperature=0.9)

# import calculator and duckduckgo tools
from langchain_community.tools import calculator, duckduckgo

# initialize tools
tools = [calculator, duckduckgo]