# for local testing and debugging
import os
from llama_index import GPTSimpleVectorIndex
import flask
from flask import request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# get api key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# # contruct index
# def construct_index(directory_path, index_name):

	# from llama_index import LLMPredictor, PromptHelper, SimpleDirectoryReader
# 	documents = SimpleDirectoryReader(directory_path, recursive=True).load_data()
# 	# define LLM
# 	llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="gpt-3.5-turbo"))
# 	service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
# 	index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
# 	index.save_to_disk(index_name)
# 	return index

# construct_index('./datasets', 'index.json')

# application
app = flask.Flask(__name__)
CORS(app)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():

	history = request.args.get('history')

	if not history:
		query = 'Instructions: you are chatting with anon about MakerDAO' + '\n\n' + 'Anon:' + '\n' + request.args.get('query') + '\n' + 'You:'
	else:
		query = 'Instructions: you are chatting with anon about MakerDAO' + '\n' + 'Anon\'s previous question: ' + history + ' ?' + '\n\n' + 'Anon:' + '\n' + request.args.get('query') + '\n' + 'You:'

	print()
	print(query)

	response = index.query(query_str=query)
	print(response.response.strip())
	print()

	return jsonify(response.response.strip())

# run app
app.run()
