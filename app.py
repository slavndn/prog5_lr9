from flask import Flask, request, jsonify
from data_base import TokenGeneration, authenticate_user
from bonus import BonusObserver
from transactions import Transactions
from flask_swagger_ui import get_swaggerui_blueprint
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, jwt_required, JWTManager
from functools import wraps

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600

jwt = JWTManager(app)
token_factory = TokenGeneration(app.config["JWT_SECRET_KEY"])
bonus_observer = BonusObserver()
transaction_service = Transactions(bonus_observer)

# Swagger UI setup
SWAGGER_URL = "/docs"
API_URL = r"/openapi.yml"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if authenticate_user(username, password):
        token = token_factory.create_token(username, password)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/users/bonus', methods=['GET'])
@jwt_required()
def get_bonus():
    current_user = get_jwt_identity()
    username = current_user['username']
    password = current_user['password']
    bonus_info = bonus_observer.get_user_bonus(username, password)
    if bonus_info:
        return jsonify(bonus_info), 200
    return jsonify({"message": "User not found"}), 404


@app.route('/users/transactions', methods=['POST'])
@jwt_required()
def add_transaction():   
    data = request.json
    current_user = get_jwt_identity()
    username = current_user['username']
    password = current_user['password']
    amount = data.get("amount")
    if amount is None:
        return jsonify({"message": "Amount is required"}), 400
    transaction_service.add_transaction(username, password, amount)
    return jsonify({"message": "Transaction added successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
