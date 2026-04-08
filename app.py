from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{'id': 1, 'name': 'Eder Evora'},
        {'id': 2, 'name': 'Luis Ramos'}]

#Search(all)
@app.route('/users', methods= ['GET'])
def get_users():
    return jsonify(users)

#Search(one)
@app.route('/users/<int:id>', methods= ['GET'])
def get_users_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

app.run(port= 5000, host= 'localhost', debug= True)

