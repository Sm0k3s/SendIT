from datetime import datetime
from werkzeug.security import generate_password_hash
from .database import Database as db

# db.initialize("dbname='sendit' user='postgres' password='github' host='localhost'")


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
#test
# user = UserModel('Kenny', 'Matiba', 'kilau', 'ken@ken.kmn', ';lk;l')
# admin = AdminModel('Kenny', 'Matiba', 'kilau', 'ken@ken.kmn', ';lk;l')
# user.save_to_db()
# admin.save_to_db()
# admin.save_to_db()
# admin.save_to_db()
# print(UserModel.find_by_username('kilau'))
# print(UserModel.find_by_id(8))
# UserModel.find_by_username('kilau')
