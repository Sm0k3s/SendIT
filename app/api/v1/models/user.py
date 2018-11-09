from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User():
    """
    A model for manipulating data for the users
    """
    Access = {
        2: 'admin',
        1 : 'user'
    }
    #database dict to store users
    database = {}
    _id = 1

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def create_user(self):
        """Creates a new user and adds the time they joined"""
        user = {
            "id": User._id,
            "username": self.username,
            "password": generate_password_hash(self.password),
            "email":self.email,
            "joined_on": datetime.now().__str__(),
            "role": User.Access[1]
        }
        User.database[User._id] = user
        User._id += 1

    @classmethod
    def get_all(cls):
        """Get all users"""
        return cls.database

    @classmethod
    def search_by_key_value(cls, key, value):
        """searches the dict database"""
        res = [i for i in cls.database.values() if i[key] == value]
        return res


class Admin(User):
    """class for Admin."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def create_user(self):
        user = {
            "id": User._id,
            "username": self.username,
            "password": generate_password_hash(self.password),
            "email":self.email,
            "joined_on": datetime.now().__str__(),
            "role": User.Access[2]
        }
        User.database[User._id] = user
        User._id += 1

###################################
#         DEBUG PRINTS            #
# #################################

User('ken','ken@ken.vk', 'pass').create_user()
Admin('groot','ken@ken.vk', 'pass').create_user()
print(User.get_all())
