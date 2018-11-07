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
        pass

    def test_get_specific_parcel(self):
        pass
