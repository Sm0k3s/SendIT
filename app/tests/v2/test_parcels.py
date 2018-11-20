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
