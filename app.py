from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

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

if __name__ == '__main__':
	app.run()