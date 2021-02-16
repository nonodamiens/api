from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_orld():
	return "Hello world !"

@app.route("/characters/")
def characters():
	characters = {
	1:"Bob",
	2:"John"
	}
	return jsonify(characters)