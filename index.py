from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import flask
from flask import request, jsonify
from flask_cors import CORS

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = flask.Flask(__name__)
CORS(app)

max_input_size = 2048
num_outputs = 2048
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="gpt-3.5-turbo", max_tokens=num_outputs)) # other models: gpt-4, gpt-3.5-turbo, text-davinci-003
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
  history = request.args.get('history')
  query = ''
  if history == 'none':
    query = 'about Maker: ' + request.args.get('query') 
  else:
    query = 'Instructions: you are chatting with anon about Maker\n\n' + history + '\n\n' + 'Anon:\n' + request.args.get('query') + '\n\nYou:\n'
  print(query)
  response = index.query(query, response_mode="default", prompt_helper=prompt_helper)
  print(response.response.strip())
  return jsonify(response.response.strip())


# for dockerised execution
def create_app():
   return app

def ask(question):
  print(question + '\n')
  response = index.query(question, response_mode="default", prompt_helper=prompt_helper)
  print(response.response.strip() + '\n\n')
  with open('result.md', 'w') as f:
    f.write(response.response.strip())

ask('what is the endgame plan?')

while True:
  q = input('Question: ')
  ask(q)
