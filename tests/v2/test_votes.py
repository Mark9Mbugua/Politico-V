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
        self.admin_sign_up = dummy_data['admin_sign_up']
        self.user_sign_up = dummy_data['user_sign_up']
        self.admin_sign_in = dummy_data['admin_sign_in']
        self.user_sign_in = dummy_data['user_sign_in']    
        self.register = dummy_data['register']
        self.vote = dummy_data['vote']

    def admin_registration(self):
        """ Register an admin"""
        response = self.client.post('/api/v2/auth/signup',data = json.dumps(self.admin_sign_up), content_type= 'application/json')
        return response
    
    def user_registration(self):
        """ Register a user"""
        response = self.client.post('/api/v2/auth/signup',data = json.dumps(self.user_sign_up), content_type= 'application/json')
        return response

    def admin_login(self):
        """Sign in Admin"""
        response = self.client.post('/api/v2/auth/signin',data = json.dumps(self.admin_sign_in), content_type= 'application/json')
        return response
    
    def user_login(self):
        """Sign in a User"""
        response = self.client.post('/api/v2/auth/signin',data = json.dumps(self.user_sign_in), content_type= 'application/json')
        return response

    def admin_token(self):
        self.admin_registration()
        self.resp = self.admin_login()
        self.tkn = json.loads(self.resp.data)
        self.token = self.tkn['token']
        auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
        return auth_header
    
    def user_token(self):
        self.user_registration()
        self.resp = self.user_login()
        self.tkn = json.loads(self.resp.data)
        self.token = self.tkn['token']
        auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
        return auth_header

class TestNormalVoteCase(TestVoteCase):

    def test_register_candidate(self):
        """Test register a voter"""
        token = self.admin_token()
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(self.register), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], "Candidate registered successfully")
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_cast_vote(self):
        """Test cast vote Request"""
        user_token = self.user_token()
        response = self.client.post('/api/v2/vote', data=json.dumps(self.vote), content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], "You successfully cast your vote")
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)
    
    def test_get_election_result(self):
        """Test GET the total votes for a particular candidate"""
        user_token = self.user_token()
        response = self.client.post('/api/v2/vote', data=json.dumps(self.vote), content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/office/1/result', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Election results retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()