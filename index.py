from dotenv import load_dotenv
import os
from pymongo import MongoClient
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import mongodb_atlas
load_dotenv()

DB_URL = os.getenv("MONGO_URL");
print(DB_URL);
if not DB_URL:
  raise Exception("DB_URL not found in .env file");
embeddings = OllamaEmbeddings();

# create the client
client = MongoClient(DB_URL)
db = client["langchain"]["vector_store"]

