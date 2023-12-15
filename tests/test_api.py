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

        response = requests.post(BASE_URL + "/api/new_task", data=request_body, headers=self.get_json_utf8_headers())
        
        self.assertEqual(201, response.status_code)
        self.assertIn(task_name, response.text)
    
    def test_create_task_with_invalid_request(self):
        response = requests.post(BASE_URL + "/api/new_task", data="", headers=self.get_json_utf8_headers())
        self.assertEqual(400, response.status_code)

    def get_json_utf8_headers(self):
        return {"Content-Type": "application/json", "charset": "utf-8"}

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

if __name__ == '__main__':
    unittest.main()
