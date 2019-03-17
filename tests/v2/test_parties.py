from tests.v2.base_test import BaseTest
import json


class TestPartyRequestCase(BaseTest):
    """Test valid requests"""

    def test_post_party(self):
        """Test POST a party Request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_parties(self):
        """Test GET all parties Request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
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
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/parties/1', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Jubilee', str(result))
    
    def test_edit_specific_party(self):
        """Test PATCH one party request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political party updated successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
    
    def test_delete_specific_party(self):
        """ Test DELETE one party request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.delete('/api/v2/parties/1', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political Party deleted successfully')
        self.assertEqual(response.status_code, 200)

class TestBadRequestCase(BaseTest):

    def test_party_less_keys(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party_less_keys), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Check if all fields exist')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_hq_add_not_spaces_int_str(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hq_add_not_spaces_int_str), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], '.... should have letters. It may also have digits and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hq_add_no_str(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hq_add_no_str), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], '106106 should have letters too')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_party_name_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party_name_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'No field should be a space')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hqAddress_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hqAddress_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'No field should be a space')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "No field should be a space")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_party_name_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party_name_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Ensure no field is blank')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_hqAddress_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.hqAddress_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Ensure no field is blank')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Ensure no field is blank")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_scheme(self):
        """Test POST party logoUrl no scheme"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_scheme), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format "
                        "'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_netloc(self):
        """Test POST party logoUrl no netloc"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_netloc), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format "\
                        "'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_logoUrl_no_path(self):
        """Test POST party logoUrl no path"""
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.logoUrl_no_path), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "logoUrl should be in the example format "\
                        "'https://www.twitter.com/profile/img.jpg'")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_no_name_key(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.edit_party_no_name_key), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.edit_party_no_name_key), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name key is missing')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.party_name_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Party name is required')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_edit_party_name_not_purely_alpha_and_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/1', data=json.dumps(self.party_name_not_purely_alpha_and_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Name should only have letters and spaces')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_party_exists(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.post('/api/v2/parties', data=json.dumps(self.same_party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party already exists')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    

class TestNotFoundCase(BaseTest):
       
    def test_get_specific_party_invalid_id(self):
        """Test GET a specific party but with invalid Id"""
        user_token = self.user_token()
        response = self.client.get('/api/v2/parties/300', data=json.dumps(self.party), 
                                    content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)

    def test_delete_specific_party_invalid_id(self):
        """Test DELETE specific party invalid id request"""
        token = self.admin_token()
        response = self.client.delete('/api/v2/parties/106', data=json.dumps(self.party), 
                                        content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
    
    def test_patch_invalid_party_id(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.patch('/api/v2/parties/3000', data=json.dumps(self.party), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political party cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)