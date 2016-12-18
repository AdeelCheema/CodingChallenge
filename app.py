from flask import Flask, jsonify, request, make_response, render_template
from flask_cors import CORS, cross_origin
import json
import CodingChallenge
import urllib

app = Flask(__name__)
cors = CORS(app, resources={"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
	"""
	Returns 404 error upon inavlid endpoint
	"""
	return make_response(jsonify({"Usage": "Please make POST request to /api/containsOrigi with 'vertices' as key and comma separated coordinates as Values"}), 404)

@app.route("/api/containsOrigin", methods=["POST"])
def return_contains_origin():
	"""
	Returns True if the given triangle encloses the origin,
	returns 400 (BAD REQUEST) on invalid triangle
	"""
	try:
		vertices = urllib.unquote(urllib.unquote(request.form['vertices']))
		main_triangle = CodingChallenge.Triangle(*vertices.split(","))
		return jsonify(main_triangle.contains_origin())
	except TypeError:
		return make_response("Please provide a valid tringle with 6 vertices", 400)

if __name__ == "__main__":
	app.run(debug=True)