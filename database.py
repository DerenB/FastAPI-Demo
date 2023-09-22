from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Get Secret Variables
load_dotenv()
connection_string = os.getenv("ConnectionString")
connection_port = os.getenv("MongoPort")

# Connect to MongoDB
client = MongoClient(connection_string, connection_port)
db = client["A-Test-Connection"]