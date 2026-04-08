from flask import Flask, jsonify, request

app = Flask(__name__)

<<<<<<< HEAD
users = [{'id': 1, 'name': 'Eder Evora'},
        {'id': 2, 'name': 'Luis Ramos'}]

#Search(all)
=======
users = [{'name': 'Eder Evora'},
        {'name': 'Luis Ramos'}]

>>>>>>> 5c29af0a9a492a44a45f8a9ba1b497646ea90eed
@app.route('/users', methods= ['GET'])
def get_users():
    return jsonify(users)

<<<<<<< HEAD
#Search(one)
@app.route('/users/<int:id>', methods= ['GET'])
def get_users_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

=======
>>>>>>> 5c29af0a9a492a44a45f8a9ba1b497646ea90eed
app.run(port= 5000, host= 'localhost', debug= True)

