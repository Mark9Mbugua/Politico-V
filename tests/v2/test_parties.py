import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data
from app.db_config import drop_test_tables, init_test_db

class TestElectionsCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            init_test_db()
        self.party = dummy_data['party']
        self.party_less_keys = dummy_data['party_less_keys']
        self.edit_party_no_name_key = dummy_data['edit_party_no_name_key']
        self.hq_add_not_spaces_int_str = dummy_data['hq_add_not_spaces_int_str']
        self.hq_add_no_str = dummy_data['hq_add_no_str']
        self.party_name_blank = dummy_data['party_name_blank']
        self.hqAddress_blank = dummy_data['hqAddress_blank']
        self.logoUrl_blank = dummy_data['logoUrl_blank']
        self.logoUrl_no_scheme = dummy_data['logoUrl_no_scheme']
        self.logoUrl_no_netloc = dummy_data['logoUrl_no_netloc']
        self.logoUrl_no_path = dummy_data['logoUrl_no_path']
        self.party_name_not_purely_alpha_and_space = dummy_data['party_name_not_purely_alpha_and_space']
        self.admin_sign_up = dummy_data['admin_sign_up']
        self.user_sign_up = dummy_data['user_sign_up']
        self.admin_sign_in = dummy_data['admin_sign_in']
        self.user_sign_in = dummy_data['user_sign_in']
        self.new_party = dummy_data['new_party']

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

class TestPartyRequestCase(TestElectionsCase):
    """Test valid requests"""

    def test_post_party(self):
        """Test POST a party Request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_parties(self):
        """Test GET all parties Request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/parties', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political parties retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Jubilee', str(result))

    def test_get_specific_party(self):
        """Test GET one party request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/parties/2', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        #self.assertIn('Legislative', str(result))
    
    def test_edit_specific_party(self):
        """Test PATCH one party request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/2', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party updated successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_delete_specific_party(self):
        """ Test DELETE one party request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.delete('/api/v2/parties/1', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party deleted successfully')
        self.assertEqual(response.status_code, 200)

class TestBadRequestCase(TestElectionsCase):

    def test_party_less_keys(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party_less_keys), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hq_add_not_spaces_int_str(self):
        token = self.admin_token()
        response = self.client.post('/api/v1/parties', data=json.dumps(self.hq_add_not_spaces_int_str), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress should have letters, spaces and numbers only')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hq_add_no_str(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hq_add_no_str), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress should have letters too')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_party_name_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party_name_blank), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hqAddress_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hqAddress_blank), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_blank), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_scheme(self):
        """Test POST party logoUrl no scheme"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_scheme), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_netloc(self):
        """Test POST party logoUrl no netloc"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_netloc), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_path(self):
        """Test POST party logoUrl no path"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_path), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_no_name_key(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.edit_party_no_name_key), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.edit_party_no_name_key), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name key is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/2', data=json.dumps(self.party_name_blank), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_not_purely_alpha_and_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/2', data=json.dumps(self.party_name_not_purely_alpha_and_space), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Name should also have letters and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    

class TestNotFoundCase(TestElectionsCase):
       
    def test_get_specific_party_invalid_id(self):
        """Test GET a specific party but with invalid Id"""
        user_token = self.user_token()
        response = self.client.get('/api/v2/parties/300', data=json.dumps(self.party), content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)

    def test_delete_specific_party_invalid_id(self):
        """Test DELETE specific party invalid id request"""
        token = self.admin_token()
        response = self.client.delete('/api/v2/parties/106', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
    
    def test_patch_invalid_party_id(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/3000', data=json.dumps(self.party), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)

    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()