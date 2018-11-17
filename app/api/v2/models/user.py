from datetime import datetime
from werkzeug.security import generate_password_hash
from database import Database

db = Database()
db.initialize("dbname='sendit' user='postgres' password='smokes' host='localhost'")

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
        query = """INSERT INTO users(firstname,surname,username,email,password,
        role,joined_on) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id
        """
        tup = (self.firstname, self.surname, self.username, self.email, self.password,
             self.role, self.joined_on)
        db.insert(query, tup)

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
