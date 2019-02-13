import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data
from app.db_config import create_test_tables, drop_test_tables, test_init_db

conn = test_init_db()

class TestElectionsCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.party = dummy_data['party']
        self.conn = psycopg2.connect(os.getenv('TEST_DATABASE_URL'))
        with self.app.app_context():
            create_test_tables()

class TestPartyRequestCase(TestElectionsCase):
    """Test valid requests"""

    def test_post_party(self):
        """Test POST a party Request"""
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_parties(self):
        """Test GET all parties Request"""
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v2/parties')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political parties retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Jubilee', str(result))

    def test_get_specific_party(self):
        """Test GET one party request"""
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v2/parties/1')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Muthaiga', str(result))
    
    def test_edit_specific_party(self):
        """Test PATCH one party request"""
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party updated successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_delete_specific_party(self):
        """
        Test DELETE one party request
        """
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.delete('/api/v2/parties/1')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party deleted successfully')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()