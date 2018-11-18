"""Module to test user routes"""
import json
from .base_test import BaseTest


class TestUser(BaseTest):
    """User tests class"""

    def test_user_signup(self):
        """Tests that a user can sign up"""
        resp = self.client.post('/api/v2/auth/signup', data=json.dumps(self.new_user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'user groot created')

    def test_user_login(self):
        """Tests if a user can signin"""
        # signup a new user
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.new_user),
                         content_type='application/json')
        # Login the newly created user
        resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'login successful')
        self.assertIn('token',json.loads(resp.get_data(as_text=True)))

    def test_unknown_username_cant_login(self):
        """Tests an unknown user cant login"""

        resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.invalid_),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'User does not exist please sign up')