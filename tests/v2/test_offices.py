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
        self.office = dummy_data['office']
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
        self.admin_sign_up = dummy_data['admin_sign_up']
        self.user_sign_up = dummy_data['user_sign_up']
        self.admin_sign_in = dummy_data['admin_sign_in']
        self.user_sign_in = dummy_data['user_sign_in']
    
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
    

class TestOfficeRequestCase(TestElectionsCase):
    def test_post_office(self):
        """Test POST an office Request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json', headers=token)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Political office created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_offices(self):
        """Test GET all offices Request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/offices', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'All political offices retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))
    
    def test_get_specific_office(self):
        """Test GET one office request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/offices/1', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))

class TestBadRequestCase(TestElectionsCase):
    
    def test_office_less_keys(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.office_less_keys), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_invalid_office_type(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.invalid_office_type), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Office type must either be Legislative, Executive or County')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_president(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_president), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_prime_minister(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_prime_minister), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_legislative_mismatch_governor(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_governor), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_mca(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_mca), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_governor(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_governor), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_senator(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_senator), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_mp(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_mp), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_women_rep(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_women_rep), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_mca(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_mca), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_president(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_president), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_prime_minister(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_prime_minister), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_senator(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_senator), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_mp(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_mp), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_county_mismatch_women_rep(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_women_rep), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
class TestNotFoundCase(TestElectionsCase):
    
    def test_get_specific_office_invalid_id(self):
        """Test GET specific party invalid id request"""
        user_token = self.user_token()
        response = self.client.get('/api/v2/offices/106', data=json.dumps(self.office), content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
    
    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()