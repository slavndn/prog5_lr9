from flask_jwt_extended import create_access_token
from datetime import timedelta

class TokenGeneration:
    def __init__(self, secret_key, expires_in=3600):
        self.secret_key = secret_key
        self.expires_in = expires_in

    def create_token(self, username: str, password: str):
        return create_access_token(identity={'username': username, 'password': password}, expires_delta=timedelta(seconds=self.expires_in))


users = {"Jonh": "password1", "user2": "password2"}

def authenticate_user(username, password):
    return users.get(username) == password
