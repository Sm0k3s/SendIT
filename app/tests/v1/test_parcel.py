import json
from app.api.v1.models.parcel import Parcel
from basetest import BaseTest

class TestParcel(BaseTest):

    def test_create_parcel(self):
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.order), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_all_parcels(self):
        resp = self.client.get('/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_parcel(self):
        """Cancels the delivery order that matches the id provided"""
        #creates a parcel order first
        self.client.post('/api/v1/parcels', data=json.dumps(self.order), content_type='application/json')
        #change cancels the parcel order
        resp = self.client.put('/api/1/cancel', data=json.dumps(), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_specific_parcel(self):
        """Gets a parcel that matches the id provided"""
        self.client.post('/api/v1/parcels', data=json.dumps(self.order), content_type='application/json')
        resp = self.client.get('/api/v1/parcels/1')
        self.assertEqual(resp.status_code, 200)
