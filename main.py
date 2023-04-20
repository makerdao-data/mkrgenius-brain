from llama_index import GPTSimpleVectorIndex
import flask
from flask import request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# load credentials from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = flask.Flask(__name__)
CORS(app)

#load pre-made index
index = GPTSimpleVectorIndex.load_from_disk('index.json')

@app.route('/ask', methods=['GET'])
def ask():
	
	history = request.args.get('history')

	if not history:
		query = 'Instructions: you are chatting with anon about MakerDAO' + '\n\n' + 'Anon:' + '\n' + request.args.get('query') + '\n' + 'You:'
	else:
		query = 'Instructions: you are chatting with anon about MakerDAO' + '\n' + 'Anon\'s previous question: ' + history + ' ?' + '\n\n' + 'Anon:' + '\n' + request.args.get('query') + '\n' + 'You:'

	response = index.query(query_str=query)
	return jsonify(response.response.strip())

if __name__ == "__main__":
	app.run(debug=False)
