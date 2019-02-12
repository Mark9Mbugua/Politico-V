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

class TestPartyRequestCase(TestElectionsCase):
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
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/parties')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political parties retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Jubilee', str(result))

    def test_get_specific_party(self):
        """Test GET one party request"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/parties/1')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Muthaiga', str(result))
    
    def test_edit_specific_party(self):
        """Test PATCH one party request"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party updated successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_delete_specific_party(self):
        """
        Test DELETE one party request
        """
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.delete('/api/v1/parties/1')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party deleted successfully')
        self.assertEqual(response.status_code, 200)

class TestBadRequestCase(TestElectionsCase):

    def test_party_less_keys(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party_less_keys), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hq_add_not_spaces_int_str(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.hq_add_not_spaces_int_str), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress should have letters, spaces and numbers only')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hq_add_no_str(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.hq_add_no_str), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress should have letters too')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_party_name_blank(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party_name_blank), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hqAddress_blank(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.hqAddress_blank), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'hqAddress is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_blank(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.logoUrl_blank), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_scheme(self):
        """Test POST party logoUrl no scheme"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.logoUrl_no_scheme), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_netloc(self):
        """Test POST party logoUrl no netloc"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.logoUrl_no_netloc), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_path(self):
        """Test POST party logoUrl no path"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.logoUrl_no_path), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_no_name_key(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.edit_party_no_name_key), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v1/parties/1', data=json.dumps(self.edit_party_no_name_key), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name key is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_blank(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v1/parties/1', data=json.dumps(self.party_name_blank), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_not_purely_alpha_and_space(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v1/parties/1', data=json.dumps(self.party_name_not_purely_alpha_and_space), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Name should only have letters and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    

class TestNotFoundCase(TestElectionsCase):
       
    def test_get_specific_party_invalid_id(self):
        """Test GET a specific party but with invalid Id"""
        response = self.client.get('/api/v1/parties/300', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)

    def test_delete_specific_party_invalid_id(self):
        """Test DELETE specific party invalid id request"""
        response = self.client.delete('/api/v1/parties/106', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
    
    def test_patch_invalid_party_id(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.patch('/api/v1/parties/3000', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
        

        
        
    


    