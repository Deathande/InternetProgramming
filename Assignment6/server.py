import sqlite3
import json
import re
from flask import Flask

app = Flask("Areas")
db = "measures.sqlite"
digit = re.compile("^\d+$")

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def welcome():
	msg = "measurement server v1.0"
	return msg

@app.route("/area", methods=['GET'])
def get_area():
	con = sqlite3.connect(db)
	curse = con.cursor()
	ret = curse.execute("SELECT * FROM area")
	data = []
	for item in ret:
		data.append({'id': item[0], 'area': item[1], 'x': item[2], 'y': item[3]})
	return json.dumps(data)

@app.route('/area/<ident>/location', methods=['GET'])
def get_location_id(ident):
	if digit.match(ident) == None:
		return "Invalid identifier" + str(ident)
	con = sqlite3.connect(db)
	curse = con.cursor()
	ret = curse.execute("SELECT * FROM location WHERE location_area=?", ident)
	data = []
	for item in ret: 
		data.append({'location id': item[0], 'name': item[1], 'altitude': item[2]})
	return json.dumps(data)

@app.route('/location/<ident>/measurement', methods=['GET'])
def get_location_measurement(ident):
	if digit.match(ident) == None:
		return "Invalid identifier" + str(ident)
	con = sqlite3.connect(db)
	curse = con.cursor()
	ret = curse.execute("SELECT * FROM measurement WHERE measurement_location=?", (ident,))
	data = []
	for item in ret:
		data.append({'measurement id': item[0], 'value': item[1]})
	return json.dumps(data)

@app.route('/area/<ident>/category', methods=['GET'])
def get_area_category(ident):
	if digit.match(ident) == None:
		return "Invalid identifier" + str(ident)
	con = sqlite3.connect(db)
	curse = con.cursor()
	cat_id = con.execute(
	"SELECT category_id FROM category_area WHERE area_id=?", (ident,))
	cat_id = cat_id.fetchone()
	cat = con.execute(
	"SELECT * FROM category WHERE category_id=?", cat_id)
	data = []
	for item in cat:
		data.append({
			'category_id': item[0],
			'name': item[1],
			'description': item[2]
		})
	return json.dumps(data)

@app.route('/area/<ident>/average_measurement', methods=['GET'])
def get_average_mesasurement(ident):
	if digit.match(ident) == None:
		return "Invalid identifier" + str(ident)
	con = sqlite3.connect(db)
	curse = con.cursor()
	la = curse.execute(
	"SELECT location_id FROM location WHERE location_area=?", (ident,))
	s = 0.0
	total_size = 0
	for item in la:
		measurements = curse.execute(
			"SELECT value FROM measurement WHERE measurement_location=?",
			item)
		for measure in measurements:
			total_size += 1
			s += float(measure[0])
	s /= total_size
	return json.dumps(s)

@app.route('/area/<ident>/number_locations', methods=['GET'])
def get_num_locations(ident):
	if digit.match(ident) == None:
		return "Invalid identifier" + str(ident)
	con = sqlite3.connect(db)
	curse = con.cursor()
	areas = curse.execute(
	"SELECT * from location WHERE location_area=?", (ident,))
	total = 0
	for item in areas:
		total += 1
	return json.dumps(total)

if __name__ == '__main__':
	app.run()
