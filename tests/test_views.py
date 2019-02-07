import unittest
import os
import json
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data

class TestElectionsCase(unittest.TestCase):

    def setUp(self):
        app = create_app(config_name="testing")
        self.client = app.test_client()
        self.party = dummy_data['party']
        self.office = dummy_data['office']

class TestNormalRequestCase(TestElectionsCase):
    """Test valid requests"""

    def test_post_party(self):
        """Test POST a party Request"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_parties(self):
        """Test GET all parties Request"""
        response = self.client.get('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political parties retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)

    def test_get_specific_party(self):
        """Test GET one party request"""
        response = self.client.get('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party has been successfully retrieved')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_edit_specific_party(self):
        """Test PATCH one party request"""
        response = self.client.patch('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party updated successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_delete_specific_party(self):
        """Test DELETE one party request"""
        response = self.client.delete('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party has been deleted successfully')
        self.assertEqual(response.status_code, 200)
    
    def test_post_office(self):
        """Test POST an office Request"""
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_offices(self):
        """Test GET all offices Request"""
        response = self.client.get('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political offices retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_get_specific_office(self):
        """Test GET one office request"""
        response = self.client.get('/api/v1/offices/1', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office has been successfully retrieved')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)



