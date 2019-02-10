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
        self.party_less_keys = dummy_data['party_less_keys']
        self.office_less_keys = dummy_data['office_less_keys']
        self.hq_add_not_spaces_int_str = dummy_data['hq_add_not_spaces_int_str']
        self.hq_add_no_str = dummy_data['hq_add_no_str']
        self.party_name_blank = dummy_data['party_name_blank']
        self.hqAddress_blank = dummy_data['hqAddress_blank']
        self.logoUrl_blank = dummy_data['logoUrl_blank']
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
        self.logoUrl_no_scheme = dummy_data['logoUrl_no_scheme']
        self.logoUrl_no_netloc = dummy_data['logoUrl_no_netloc']
        self.logoUrl_no_path = dummy_data['logoUrl_no_path']


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
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political parties retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)

    def test_get_specific_party(self):
        """Test GET one party request"""
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
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
        response = self.client.delete('/api/v1/parties/1', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party deleted successfully')
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
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political offices retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_get_specific_office(self):
        """Test GET one office request"""
        response = self.client.post('/api/v1/offices', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        response = self.client.get('/api/v1/offices/1', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)

class TestBadRequestCase(TestElectionsCase):

    def test_party_less_keys(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.party_less_keys), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_less_keys(self):
        response = self.client.post('/api/v1/parties', data=json.dumps(self.office_less_keys), content_type='application/json')
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

class TestNotFoundCase(TestElectionsCase):   
    def test_get_specific_party_invalid_id(self):
        """Test GET a specific party but with invalid Id"""
        response = self.client.get('/api/v1/parties/300', data=json.dumps(self.party), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
        
    def test_edit_specific_party_invalid_id(self):
        """Test PATCH specific party invalid id request"""
        response = self.client.patch('/api/v1/parties/106', data=json.dumps(self.party), content_type='application/json')
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
    
    def test_get_specific_office_invalid_id(self):
        """Test GET specific party invalid id request"""
        response = self.client.get('/api/v1/offices/106', data=json.dumps(self.office), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
        

        
        
    


    