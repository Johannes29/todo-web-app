import json
import unittest
import subprocess
import requests

BASE_URL = "http://localhost:5678"

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen("flask --app api/main run --host localhost --port 5678")

    # TODO Implement create task feature so that this test passes
    def test_create_task(self):
        task_name = "Test task 123"
        request_body = json.dumps({
            "name": task_name
        })

        response = requests.post(BASE_URL + "/api/new_task", data=request_body)
        
        self.assertEqual(201, response.status_code)
        self.assertIn(task_name, response.text)

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
