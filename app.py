from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Aditya 🚀 Flask App Running!"

@app.route('/data')
def data():
    return {
        "name": "Aditya",
        "role": "DevOps Learner",
        "status": "Learning Docker 🚀"
    }

@app.route('/hello')
def hello():
    return "Hello Aditya Learning DevOps 🚀"

from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json(silent=True)

    if not data:
    return {"error": "Name is required"}, 400

    name = data.get("name")

    return {
        "message": f"Hello {name}, data received successfully 🚀"
    }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)