"""Module to to declare test dependencies"""
import unittest
from run import create_app
from app.api.v2.models.database import Database as db

class BaseTest(unittest.TestCase):
    """The base test class"""

    def setUp(self):
        """Initializes the test client"""
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()
        self.order = {
            "title": "Abagof",
            "destination": "Kajiado  ",
            "weight": 5,
            "pickup_location": "Nairobi",
            "description": ""
        }
        self.new_user = {
            "firstname":"who",
	        "surname":"areyou",
            "username": "groot",
            "email": "groot@gmail.com",
            "password": "iamgroot"
        }
        self.unique_user = {
            "username": "laca",
            "email": "laca@gmail.com",
            "password": "iamgroot"
        }
        self.user = {
            "username": "groot",
            "password": "iamgroot"
        }
        self.invalid_user = {
            "username": "groot",
            "email": "    ",
            "password": "iamgroot"
        }

    def tearDown(self):
        """Drops all tables when the test client is done"""
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
