from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

from models import Hat

@app.route("/")
def hello_world():
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