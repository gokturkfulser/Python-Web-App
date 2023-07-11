from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'World',
        'message': 'Hello, World!'
    }
    return jsonify(data)