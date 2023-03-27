import os

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'
# Don't forget to replace the above API Key!!
# Link to generate one: https://platform.openai.com/account/api-keys

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Loads the 'data' folder with all files inside it
documents = SimpleDirectoryReader('training-data', recursive=True).load_data()

# Creates a SimpleVector Index
index = GPTSimpleVectorIndex(documents)

# Queries the index with prompt
index.query("what is the endgame plan?")

# #####################################

# You might want to save the index on the disk because
# it takes too long to build one from scratch!

# Use the functions below to save/load:

# save to disk
index.save_to_disk('index.json')

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')