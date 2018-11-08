import json
from app.api.v1.models.parcel import Parcel
from .basetest import BaseTest

class TestParcel(BaseTest):

    def test_create_parcel(self):
        """Tests creation of a delivery order url=/api/v1/parcels"""
        resp = self.client.post('/api/v1/parcels', data=json.dumps(self.order),
                                               content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_all_parcels(self):
        """Tests return of all delivery orders url=/api/v1/parcels"""
        resp = self.client.get('/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_parcel(self):
        """
        Tests cancelation of the delivery order that matches
        the id provided url=/api/v1/<int:parcel_id>/cancel
        """
        #creates a parcel order first
        self.client.post('/api/v1/parcels', data=json.dumps(self.order),
                                        content_type='application/json')
        #change cancels the parcel order
        resp = self.client.put('/api/v1/parcels/1/cancel', data=json.dumps({'status':'cancel'}),
                                               content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_specific_parcel(self):
        """
        Gets a parcel that matches the id provided
        url=/api/v1/parcels/<int:parcel_id>
        """
        self.client.post('/api/v1/parcels', data=json.dumps(self.order),
                                       content_type='application/json')
        resp = self.client.get('/api/v1/parcels/1')
        self.assertEqual(resp.status_code, 200)

    def test_get_parcels_by_a_specific_user(self):
        """
        Get all the orders of the user whose id has been provided
        url=/api/v1/users/<int:user_id>/parcels
        """
        resp = self.client.get('/api/users/1/parcels/')
        self.assertEqual(resp.status_code, 200)

    def test_modify_the_destination(self):
        #create a parcel order
        self.client.post('/api/v1/parcels', data=json.dumps(self.order),
                                        content_type='application/json')
        #modify the destination
        resp = self.client.put('/api/v1/parcels/1', data=json.dumps({'destination':'new destination'}),
                                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertIn(json.loads(resp.data)['Message'], 'Parcel updated successfully')
