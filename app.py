from flask import Flask, jsonify, request

app = Flask(__name__)

#Datas
users = [
    {'id': 1, 'name': 'Eder Evora'},
    {'id': 2, 'name': 'Luis Ramos'}
]

products = [ 
    {'id': 1, 'name': 'Laptop', 'brand': 'Huawei', 'price': 30000}, 
    {'id': 2, 'name': 'Mouse', 'brand': 'Mitsai', 'price': 1500}, 
    {'id': 3, 'name': 'Telemovel', 'brand': 'Xioami Redmi', 'price': 18000} 
]

orders = [
    {
        'id': 1,
        'user_id': 1,
        'products': [1, 2], 
        'total': 31500
    },
    {
        'id': 1,
        'user_id': 2,
        'products': [3], 
        'total': 18000
    }
]

#Search(all)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

#Search(one)
@app.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

#Edit
@app.route('/products/<int:id>', methods=['PUT'])
def edit_products_by_id(id):
    product_change = request.get_json()
    for indice,product in enumerate (products):
        if product.get('id') == id:
            products[indice].update(product_change)
            return jsonify(products[indice])


app.run(port=5000, host='localhost', debug=True)