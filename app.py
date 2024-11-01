# app.py
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Classes for basic structure (optional, can omit if unnecessary)
class Product:
    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

# Endpoint to get all products
@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(data['products']), 200

# Endpoint to add a new product
@app.route('/api/v1/products', methods=['POST'])
def add_product():
    new_product = request.json
    new_product['id'] = len(data['products']) + 1
    data['products'].append(new_product)
    save_data()
    return jsonify(new_product), 201

# Function to save data back to JSON file
def save_data():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
