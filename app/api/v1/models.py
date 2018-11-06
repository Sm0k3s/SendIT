from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    """
    A model for manipulating data for the users
    """
    Access = {
        2: 'admin',
        1 : 'user'
    }

    database = {}
    _id = 1

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    @classmethod
    def create_user(cls, username, email, password):
        user = {
            "id": cls._id,
            "username": username,
            "password": generate_password_hash(password),
            "email":email,
            "role": cls.Access[2]
        }
        cls.database[cls._id] = user
        cls._id += 1
