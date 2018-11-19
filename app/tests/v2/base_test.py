"""Module to to declare test dependencies"""
import unittest
import json
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
            "firstname":"alex",
            "surname":"ndee",
            "username": "laca",
            "email": "laca@gmail.com",
            "password": "iamgroot"
        }
        self.uni = {
            "username": "laca",
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
        self.invalid_ = {
            "username": "     ",
            "password": "iamgroot"
        }
    def get_token(self):
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.unique_user),
                                content_type='application/json')
        self.resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.uni),
                                content_type='application/json')
        self.access_token = json.loads(self.resp.get_data(as_text=True))['token']
        self.auth_header = {'Authorization': 'Bearer {}'.format(self.access_token)}
        return self.auth_header

    def tearDown(self):
        """Drops all tables when the test client is done"""
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
