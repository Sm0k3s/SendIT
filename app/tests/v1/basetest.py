import unittest
from run import create_app

class BaseTest(unittest.TestCase):
    def setUp(self):
        """Initializes the test client"""
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client()
        self.order = {
			"destination": "Kajiado  ",
			"weight": 5,
			"pickup_location": "Nairobi"
		}

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

if __name__=='__main__':
    unittest.main()
