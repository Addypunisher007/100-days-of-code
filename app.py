from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)