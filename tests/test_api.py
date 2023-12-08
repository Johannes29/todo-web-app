import unittest
import subprocess
import requests

BASE_URL = "http://localhost:5678"

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen("flask --app api/main run --host localhost --port 5678")

    # This test is just a placeholder for future tests
    def test_hello_world(self):
        response = requests.get(BASE_URL)
        self.assertEqual(200, response.status_code)
        self.assertIn("hello, world", response.text.lower())
    
    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

if __name__ == '__main__':
    unittest.main()
