import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data
from app.db_config import drop_test_tables, init_test_db

class TestVoteCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            init_test_db()
        self.vote = dummy_data['vote']

class TestNormalVoteCase(TestVoteCase):

    def test_cast_vote(self):
        """Test POST a voter Request"""
        response = self.client.post('/api/v2/vote', data=json.dumps(self.vote), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "Vote has been cast successfully")
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)
    
    def test_get_election_result(self):
        """Test GET the total votes for a particular candidate"""
        response = self.client.post('/api/v2/office/1/result', data=json.dumps(self.vote), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v2/office/1/result')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All votes retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()