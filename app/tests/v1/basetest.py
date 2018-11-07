import unittest
from run import create_app

class BaseTest(unittest.Testcase):
    def setUp(self):
        self.app = create_app(config_name="TESTING")
        self.client = self.app.test_client

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None
