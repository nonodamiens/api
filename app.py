import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

USER = "postgres"
PASSWORD = os.environ.get("POSTGRES_PASS")
URL = "localhost"
DATABASE = "hat"

if not PASSWORD:
    raise ValueError("No password set for database connection")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=USER, pw=PASSWORD, url=URL, db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

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

@app.route("/hats/")
def hats():
	hats_list = db.session.query(Hat).all()
	print(hats_list)
	return "API response to set"

if __name__ == '__main__':
	app.run(debug=True)