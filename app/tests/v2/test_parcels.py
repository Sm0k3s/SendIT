"""Module to test parcel routes"""
import json
from .base_test import BaseTest


class TestParcel(BaseTest):
    """Parcel tests class"""
    def test_can_create_parcel(self):
        """Tests creation of a delivery order url=/api/v2/parcels"""
        resp = self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                                content_type='application/json',
                                headers=self.get_token())
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                         'parcel created successfully')

    def test_can_cancel_parcel(self):
        """Tests that a user can cancel a parcel"""
        self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                         content_type='application/json',
                         headers=self.get_token())

        resp = self.client.put('/api/v2/parcels/1/cancel', content_type='application/json',
                                headers=self.get_token())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                         'parcel 1 canceled')

    def test_get_parcels_by_a_specific_user(self):
        self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                         content_type='application/json',
                         headers=self.get_token())
        self.client.post('/api/v2/parcels', data=json.dumps(self.order),
                         content_type='application/json',
                         headers=self.get_token())
        resp = self.client.get('/api/v2/users/1/parcels', content_type='application/json',
                                headers=self.get_token())
        self.assertEqual(resp.status_code, 200)
        self.assertIn('all parcels',
                      json.loads(resp.get_data(as_text=True)))

    def test_cannot_cancel_nonexistent_parcel(self):
        resp = self.client.put('/api/v2/parcels/1/cancel', content_type='application/json',
                                headers=self.get_token())
        self.assertEqual(json.loads(resp.get_data(as_text=True))['message'],
                         'parcel does not exist')
