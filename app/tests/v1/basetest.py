"""Module to to declare test dependencies"""
import unittest
from run import create_app
# from app.api.v1.models.parcel import Parcel

class BaseTest(unittest.TestCase):
    """The base test class"""

    def setUp(self):
        """Initializes the test client"""
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()
        self.order = {
            "destination": "Kajiado  ",
            "weight": 5,
            "pickup_location": "Nairobi"
        }
        self.new_user = {
            "username": "groot",
            "email": "groot@gmail.com",
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
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

if __name__ == '__main__':
    unittest.main()
