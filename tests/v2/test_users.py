import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data
from app.db_config import drop_test_tables, init_test_db

class TestUserCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            init_test_db()
        self.admin_sign_up = dummy_data['admin_sign_up']
        self.user_sign_up = dummy_data['user_sign_up']
        self.admin_sign_in = dummy_data['admin_sign_in']
        self.user_sign_in = dummy_data['user_sign_in']
        self.user_less_keys = dummy_data['user_less_keys']
        self.pwd_less_char = dummy_data['pwd_less_char']
        self.pwd_no_caps = dummy_data['pwd_no_caps']
        self.pwd_all_caps = dummy_data['pwd_all_caps']
        self.pwd_no_digit = dummy_data['pwd_no_digit']
        self.firstname_all_char =  dummy_data['firstname_all_char']
        self.lastname_all_char =  dummy_data['lastname_all_char']
        self.bad_email =  dummy_data['bad_email']
        self.short_email =  dummy_data['short_email']
        self.bad_phone =  dummy_data['bad_phone']
        self.phone_not_ten_dig = dummy_data['phone_not_ten_dig']

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
        self.token = self.tkn['data']
        auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
        return auth_header
    
    def user_token(self):
        self.user_registration()
        self.resp = self.user_login()
        self.tkn = json.loads(self.resp.data)
        self.token = self.tkn['data']
        auth_header = {'Authorization': 'Bearer {}'.format(self.token)}
        return auth_header

class TestUserNormalRequestCase(TestUserCase):
    """Test valid requests"""

    def test_user_signup(self):
        """Test create a Request"""
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_sign_up), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "User signed up successfully")
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)
    
class TestUserBadRequestCase(TestUserCase):
    """Test bad requests"""    

    def test_user_less_keys(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_less_keys), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'One or more keys is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_less_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_less_char), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Password should have at least 5 characters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_pwd_no_caps(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_no_caps), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Password should have atleast one capital letter')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_all_caps(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_all_caps), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Password should have atleast one lowercase letter')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_pwd_no_digit(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_no_digit), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Password should have atleast one number')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_firstname_all_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.firstname_all_char), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'First name should only have letters and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_lastname_all_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.lastname_all_char), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Last name should only have letters and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_bad_email(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.bad_email), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Email should be in the format 'name@address.com'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_short_email(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.short_email), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Email is too short')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_bad_phone(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.bad_phone), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Phone number should have digits only')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_phone_not_ten_dig(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.phone_not_ten_dig), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Phone number should have 10 digits')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def tearDown(self):
        with self.app.app_context():
            drop_test_tables()
    

        