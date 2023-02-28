# pip install gpt_index
# pip install langchain
# pip install sentencepiece

from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import flask
from flask import request, jsonify
from flask_cors import CORS
import os

app = flask.Flask(__name__)
CORS(app)

max_input_size = 2048
num_outputs = 2048
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.2, model_name="text-davinci-003", max_tokens=num_outputs))
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

def construct_index(directory_path, index_name):
  documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()
  index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
  index.save_to_disk(index_name)
  return index

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
  history = request.args.get('history')
  query = ''
  if history == 'none':
    query = 'about MakerDAO: ' + request.args.get('query') 
  else:
    query = 'Instructions: you are chatting with anon about MakerDAO\n\n' + history + '\n\n' + 'Anon:\n' + request.args.get('query') + '\n\nYou:\n'
  print(query)
  response = index.query(query, response_mode="default", prompt_helper=prompt_helper)
  print(response.response.strip())
  return jsonify(response.response.strip())


def create_app():
    return app

# def ask(question):
#   max_input_size = 2048
#   num_outputs = 2048
#   llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.2, model_name="text-davinci-003", max_tokens=num_outputs))
#   prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)
#   print(question + '\n')
#   response = index.query(question, response_mode="default", prompt_helper=prompt_helper)
#   print(response.response.strip() + '\n\n')
  # with open('result.md', 'w') as f:
  #   f.write(response.response.strip())

# construct_index('./training-data', 'index.json')
# ask('what is the endgame plan?')

# while True:
#   q = input('Question: ')
#   ask(q)
