from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash
from flask_jwt_extended import get_jwt_identity
from .database import Database as db


class UserModel():
    """User model that will persist data to the db"""

    def __init__(self, firstname="", surname="", username="", email="", password="",
                 role="user", joined_on=datetime.now().__str__()):
        self.firstname = firstname
        self.surname = surname
        self.username = username
        self.email = email
        self.role = role
        self.password = generate_password_hash(password)
        self.joined_on = joined_on

    def save_to_db(self):
        """Saves a user into the database"""
        query = """INSERT INTO users(firstname,surname,username,email,password,
        role,joined_on) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id
        """
        tup = (self.firstname, self.surname, self.username, self.email, self.password,
             self.role, self.joined_on)
        db.insert(query, tup)

    @classmethod
    def find_by_username(cls,username):
        """Finds a user by their username"""
        query = "SELECT * FROM users WHERE username=%s"
        return db.find_one(query, (username,))

    @classmethod
    def find_by_id(cls,id):
        """Finds a user by their username"""
        query = "SELECT * FROM users WHERE id=%s"
        return db.find_one(query, (id,))

class AdminModel(UserModel):

    def __init__(self, firstname="", surname="", username="", email="", password="",
                 role="", joined_on=datetime.now().__str__()):
        super().__init__(firstname, surname, username, email, password, role, joined_on)
        self.role = "admin"


def admin(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        user = UserModel.find_by_id(get_jwt_identity())
        if user['role'] != 'admin':
            return {'message':'user not an admin please upgrade'}, 401
        # print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper
