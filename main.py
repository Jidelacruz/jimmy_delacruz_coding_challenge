import json
import logging

from flask import Flask, request

import Algo_compute_challenge

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/productionplan', methods=['POST'])
def production_plan():
    request_data = request.get_json()
    return Algo_compute_challenge.production_data(request_data)

if __name__ == '__main__':
    app.run(debug=True, port=8888)