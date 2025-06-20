#!/usr/bin/env python3
"""
Example Flask API server demonstrating backend code in directories
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Sample data storage (in production, you'd use a database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Example API!",
        "endpoints": [
            "/users - GET all users",
            "/users/<id> - GET specific user",
            "/users - POST new user",
            "/calculate - POST math calculations"
        ]
    })

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    new_user = {
        "id": max([u['id'] for u in users]) + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }
    
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    required_fields = ['num1', 'num2', 'operation']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "num1, num2, and operation are required"}), 400
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation'].lower()
        
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else None
        }
        
        if operation not in operations:
            return jsonify({"error": "Invalid operation"}), 400
        
        if operation == 'divide' and num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        
        result = operations[operation](num1, num2)
        
        return jsonify({
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        })
        
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

if __name__ == '__main__':
    print("Starting Example API Server...")
    print("Available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)