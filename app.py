import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([
        { "id": 1, "name": "Dog Food", "price": 19.99 },
        { "id": 2, "name": "Cat Food", "price": 34.99 },
        { "id": 3, "name": "Bird Seeds", "price": 10.99 }
    ])

if __name__ == '__main__':
    port = int(os.getenv("PORT", 3030))
    app.run(debug=False, host='0.0.0.0', port=port)