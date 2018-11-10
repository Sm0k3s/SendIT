"""Module to test user routes"""
import json
#from app.api.v1.models.user import User
from .basetest import BaseTest


class TestUser(BaseTest):
    """User tests class"""

    def test_user_signup(self):
        """Tests that a user can sign up"""
        resp = self.client.post('/api/v1/auth/signup', data=json.dumps(self.new_user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_user_login(self):
        """Tests if a user can signin"""
        # signup a new user
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.new_user),
                         content_type='application/json')
        # Login the newly created user
        resp = self.client.post('/api/v1/auth/login', data=json.dumps(self.user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_user_logout(self):
        """Tests if a user can logout"""
        # create a new user
        self.client.post('/api/v1/auth/signup', data=json.dumps(self.new_user),
                         content_type='application/json')
        # Login the newly created user
        self.client.post('/api/v1/auth/login', data=json.dumps(self.user),
                         content_type='application/json')
        # logout the user
        resp = self.client.delete('/api/v1/users/logout')
        self.assertEqual(resp.status_code, 200)  # logout

    def test_cant_signup_with_empty_fields(self):
        """Tests a user can cannot signup with empty(white spaces) details"""
        # create a new user with missing fields
        resp = self.client.post('/api/v1/auth/signup', data=json.dumps(self.invalid_user),
                                content_type='application/json')
        self.assertEqual(json.loads(resp.get_data(as_text=True))['Message'],
                         'One or more fields empty')
