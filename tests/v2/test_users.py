from tests.v2.base_test import BaseTest
import json


class TestUserCase(BaseTest):
    """Test valid requests"""

    def test_user_signup(self):
        """Test create a Request"""
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_sign_up), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], "User signed up successfully")
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)
    
class TestUserBadRequestCase(BaseTest):
    """Test bad requests"""    

    def test_user_less_keys(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_less_keys), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Check if all fields exist')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_less_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_less_char), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Password should not be less than 8 characters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_pwd_no_caps(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_no_caps), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Password should have at least one small letter, "\
                          "one capital letter and one number")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_all_caps(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_all_caps), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Password should have at least one small letter, "\
                          "one capital letter and one number")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_pwd_no_digit(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.pwd_no_digit), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Password should have at least one small letter, "\
                          "one capital letter and one number")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_firstname_all_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.firstname_all_char), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'De*7#@ should only have letters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_lastname_all_char(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.lastname_all_char), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Bas*7#@ should only have letters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_bad_email(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.bad_email), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Email address is invalid. Kindly enter a valid email address")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_bad_phone(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.bad_phone), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], '25471234090i should only have digits')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_phone_short(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.phone_short), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Phone number should have 12 digits " \
            "starting with the country code for example: 254712345678")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_firstname_not_string(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.firstname_not_string), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_lastname_not_string(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.lastname_not_string), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_username_not_string(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.username_not_string), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)


    def test_phone_not_string(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.phone_not_string), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_password_not_string(self):
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.password_not_string), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_user_exists(self):
        """Test if user exists"""
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_sign_up), 
                                    content_type='application/json')
        result = json.loads(response.data)
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_sign_up), 
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'User already exists')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_wrong_password(self):
        token = self.user_token()
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.wrong_password), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    
    def test_user_not_exist(self):
        token = self.user_token()
        response = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_not_exist), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)


        