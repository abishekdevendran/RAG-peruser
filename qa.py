from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_community.llms import Ollama
llm = Ollama(model="llama2", temperature=0.9)

import os
from langchain_community.utilities import SQLDatabase
DB_URL = os.getenv("SQL_URL");
db = SQLDatabase.from_uri(DB_URL)

from langchain.chains import create_sql_query_chain
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many posts are there"})
print(response)