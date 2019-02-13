import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from app.db_config import create_test_tables, drop_test_tables, test_init_db

conn = test_init_db()
class TestElectionsCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.office = {
                    'office_type' : "Legislative",
                    'name': "Member of Parliament"
                     }
        self.conn = psycopg2.connect(os.getenv('TEST_DATABASE_URL'))
        with self.app.app_context():
            create_test_tables()

class TestOfficeRequestCase(TestElectionsCase):
    
    def test_post_office(self):
        """Test POST an office Request"""
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_offices(self):
        """Test GET all offices Request"""
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v2/offices')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political offices retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))
    
    def test_get_specific_office(self):
        """Test GET one office request"""
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v2/offices/1')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))
    
    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()