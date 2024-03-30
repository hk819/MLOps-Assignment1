import unittest
from flask import json
from app import app

class FlaskRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict_route(self):
        payload = json.dumps({"features": [5.9, 3.0, 5.1, 1.8]})
        response = self.app.post('/predict', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn('prediction', data)

if _name_ == '_main_':
    unittest.main()