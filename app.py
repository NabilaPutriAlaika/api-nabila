from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulasi database
products = [
    { "id": 1, "name": "EXO Lightstick", "description": "Official EXO Lightstick Ver.3", "price": 500000, "stock": 10 },
    { "id": 2, "name": "EXO T-Shirt", "description": "Official EXO Merchandise T-Shirt", "price": 300000, "stock": 20 }
]

users = [
    { "id": 1, "username": "exofan88", "password": "securepassword123", "email": "exofan88@example.com", "address": "Seoul" }
]

orders = []

# 1. **Produk Endpoint**

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product)

@app.route('/api/v1/products', methods=['POST'])
def add_product():
    new_product = {
        "id": len(products) + 1,
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price'],
        "stock": request.json['stock']
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/api/v1/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    product['name'] = request.json.get('name', product['name'])
    product['description'] = request.json.get('description', product['description'])
    product['price'] = request.json.get('price', product['price'])
    product['stock'] = request.json.get('stock', product['stock'])
    
    return jsonify(product)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [p for p in products if p['id'] != id]
    return jsonify({"message": "Product deleted"}), 204

# 2. **Pengguna Endpoint**

@app.route('/api/v1/users/register', methods=['POST'])
def register_user():
    new_user = {
        "id": len(users) + 1,
        "username": request.json['username'],
        "password": request.json['password'],  # Note: Passwords should be hashed in a real app
        "email": request.json['email'],
        "address": request.json['address']
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/v1/users/login', methods=['POST'])
def login_user():
    user = next((u for u in users if u['username'] == request.json['username'] and u['password'] == request.json['password']), None)
    if not user:
        return jsonify({"message": "Invalid credentials"}), 400
    
    # Placeholder token for simplicity
    token = "mock-jwt-token"
    return jsonify({"message": "Login successful", "token": token})

@app.route('/api/v1/users/profile', methods=['GET'])
def get_user_profile():
    user = users[0]  # Simulasi profil pengguna (autentikasi tidak diimplementasikan di sini)
    return jsonify(user)

# 3. **Pesanan Endpoint**

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    new_order = {
        "id": len(orders) + 1,
        "userId": request.json['userId'],
        "items": request.json['items'],
        "totalAmount": request.json['totalAmount'],
        "shippingAddress": request.json['shippingAddress'],
        "paymentMethod": request.json['paymentMethod']
    }
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_order(orderId):
    order = next((o for o in orders if o['id'] == orderId), None)
    if not order:
        return jsonify({"message": "Order not found"}), 404
    return jsonify(order)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
