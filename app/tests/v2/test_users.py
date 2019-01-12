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
                                    'user groot successfully signed up')

    def test_user_login(self):
        """Tests if a user can signin"""
        # signup a new user
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.new_user),
                         content_type='application/json')
        # Login the newly created user
        resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['Message'],
                                    'login successful')
        self.assertIn('token',json.loads(resp.get_data(as_text=True)))

    def test_unknown_username_cant_login(self):
        """Tests an unknown user cant login"""

        resp = self.client.post('/api/v2/auth/login', data=json.dumps(self.invalid_),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'please enter a name with atleast 3 characters')

    def test_user_cannot_change_status_of_parcel(self):
        self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                                content_type='application/json',
                                headers=self.get_token())
        resp = self.client.put('/api/v2/parcels/1/status', content_type='application/json',
                                 headers=self.get_token())
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'user not an admin please upgrade')

    def test_admin_can_change_status_of_parcel(self):
        self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                                content_type='application/json',
                                headers=self.get_token())
        resp = self.client.put('/api/v2/parcels/1/status', content_type='application/json',
                                 headers=self.get_admin_token())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'updated status')

    def test_admin_can_change_present_location(self):
        local = {'location':'currentlocale'}
        resp = self.client.put('/api/v2/parcels/1/presentLocation', data=json.dumps(local),
                                content_type='application/json',
                                 headers=self.get_admin_token())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'parcel updated successfully')

    def test_admin_can_be_registered(self):
        resp = self.client.post('/api/v2/admin/signup', data=json.dumps(self.new_user),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                                    'user groot successfully signed up')
