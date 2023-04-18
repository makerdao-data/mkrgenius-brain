# for local testing and debugging

import sys
import logging
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
import flask
from flask import request, jsonify
from flask_cors import CORS

# logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# get api key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# LLM definition
max_input_size = 2048
num_outputs = 2048
model_name = "gpt-3.5-turbo" # other models: gpt-4, gpt-3.5-turbo, text-davinci-003
temperature = 0.01
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=temperature, model_name=model_name, max_tokens=num_outputs))
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

# contruct index
def construct_index(directory_path, index_name):
  documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()
  index = GPTSimpleVectorIndex.from_documents(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
  index.save_to_disk(index_name)
  return index

# application
app = flask.Flask(__name__)
CORS(app)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
  history = request.args.get('history')
  query = ''
  if history == 'none':
    query = 'Instructions: you are chatting with anon about MakerDAO\n\n' + '\n\n' + 'Anon:\n' + request.args.get('query') + '\n\nYou:\n'
  else:
    query = 'Instructions: you are chatting with anon about MakerDAO\n\n' + history + '\n\n' + 'Anon:\n' + request.args.get('query') + '\n\nYou:\n'
  print(query)
  response = index.query(query, response_mode="default", prompt_helper=prompt_helper)
  print(response.response.strip())
  return jsonify(response.response.strip())

# construct index
#construct_index('./documents', 'index_new.json')

# run app
app.run()