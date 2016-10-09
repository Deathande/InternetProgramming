import sqlite3
import json
from flask import Flask

app = Flask("Areas")

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def welcome():
	msg = "measurement server v1.0"
	return msg

@app.route("/area", methods=['GET'])
def get_area():
	pass

if __name__ == '__main__':
	app.run()
