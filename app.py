from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{'name': 'Eder Evora'},
        {'name': 'Luis Ramos'}]

@app.route('/users', methods= ['GET'])
def get_users():
    return jsonify(users)

app.run(port= 5000, host= 'localhost', debug= True)

