from flask import Flask

app = Flask(__name__)

data = []

@app.route("/")
def hello():
    return "Hey Welcome to Our AI"

@app.route('/uploadData', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route('/See Data')
def display():
    return data