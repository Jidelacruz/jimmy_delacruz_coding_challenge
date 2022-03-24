
from flask import Flask, request, render_template

import Algo_compute_challenge

app = Flask(__name__)
from flask_socketio import SocketIO, emit
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/productionplan', methods=['POST'])
def production_plan():
    request_data = request.get_json()
    res = Algo_compute_challenge.production_data(request_data)
    socketio.emit("message",res,broadcast=True)
    return res


if __name__ == '__main__':
    socketio.run(app,debug=True, port=8888)