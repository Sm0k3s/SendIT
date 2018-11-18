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
