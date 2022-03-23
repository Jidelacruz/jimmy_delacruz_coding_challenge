
from flask import Flask, request, render_template

import Algo_compute_challenge

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./views/index.html')

@app.route('/productionplan', methods=['POST'])
def production_plan():
    request_data = request.get_json()
    return Algo_compute_challenge.production_data(request_data)

if __name__ == '__main__':
    app.run(debug=True, port=8888)