from flask import (Flask, render_template, request,
					redirect, url_for, make_response)
from options import DEFAULTS
import json

app = Flask(__name__)


def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data

@app.route('/')
def index():
	data = get_saved_data()
	return render_template("index.html", saves=data)

@app.route('/builder')
def builder():
	return render_template('builder.html',
							saves=get_saved_data(),
							options=DEFAULTS)

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('builder')))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response

app.run(debug = True, host='0.0.0.0', port = 8080)