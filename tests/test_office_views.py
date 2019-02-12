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
        self.office = dummy_data['office']
        self.office_two = dummy_data['office_two']
        self.office_less_keys = dummy_data['office_less_keys']
        self.invalid_office_type = dummy_data['invalid_office_type']
        self.legislative_mismatch_president = dummy_data['legislative_mismatch_president']
        self.legislative_mismatch_prime_minister = dummy_data['legislative_mismatch_prime_minister']
        self.legislative_mismatch_governor = dummy_data['legislative_mismatch_governor']
        self.legislative_mismatch_mca = dummy_data['legislative_mismatch_mca']
        self.executive_mismatch_governor = dummy_data['executive_mismatch_governor']
        self.executive_mismatch_senator = dummy_data['executive_mismatch_senator']
        self.executive_mismatch_mp = dummy_data['executive_mismatch_mp']
        self.executive_mismatch_women_rep = dummy_data['executive_mismatch_women_rep']
        self.executive_mismatch_mca = dummy_data['executive_mismatch_mca']
        self.county_mismatch_president = dummy_data['county_mismatch_president']
        self.county_mismatch_prime_minister = dummy_data['county_mismatch_prime_minister']
        self.county_mismatch_senator = dummy_data['county_mismatch_senator']
        self.county_mismatch_mp = dummy_data['county_mismatch_mp']
        self.county_mismatch_women_rep = dummy_data['county_mismatch_women_rep']

class TestOfficeRequestCase(TestElectionsCase):
    
    def test_post_office(self):
        """Test POST an office Request"""
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_offices(self):
        """Test GET all offices Request"""
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office_two), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/offices')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political offices retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('President', str(result))
    
    def test_get_specific_office(self):
        """Test GET one office request"""
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/offices/2')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))
    
class TestBadRequestCase(TestElectionsCase):
    
    def test_office_less_keys(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.office_less_keys), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_invalid_office_type(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.invalid_office_type), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Office type must either be Legislative, Executive or County')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_president(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.legislative_mismatch_president), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_prime_minister(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.legislative_mismatch_prime_minister), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_legislative_mismatch_governor(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.legislative_mismatch_governor), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_mca(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.legislative_mismatch_mca), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_governor(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.executive_mismatch_governor), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_senator(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.executive_mismatch_senator), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_mp(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.executive_mismatch_mp), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_women_rep(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.executive_mismatch_women_rep), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_mca(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.executive_mismatch_mca), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_president(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.county_mismatch_president), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_prime_minister(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.county_mismatch_prime_minister), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_senator(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.county_mismatch_senator), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_mp(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.county_mismatch_mp), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)    
    def test_county_mismatch_women_rep(self):
        response = self.client.post('/api/v1/offices', data=json.dumps(self.county_mismatch_women_rep), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
class TestNotFoundCase(TestElectionsCase):
    
    def test_get_specific_office_invalid_id(self):
        """Test GET specific party invalid id request"""
        response = self.client.get('/api/v1/offices/106', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)