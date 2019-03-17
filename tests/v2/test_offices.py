from tests.v2.base_test import BaseTest
import json

class TestOfficeRequestCase(BaseTest):
    def test_post_office(self):
        """Test POST an office Request"""
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Political office created successfully')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('data' in result)

    def test_get_all_offices(self):
        """Test GET all offices Request"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
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
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/offices/1', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Political office retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)
        self.assertIn('Legislative', str(result))

class TestBadRequestCase(BaseTest):

    def test_office_type_not_string(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_type_not_string), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_name_not_string(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_name_not_string), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_location_not_string(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.location_not_string), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'All fields should be in string format')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_type_not_letters(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_type_not_letters), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'County 106 should only have letters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_name_not_letters(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_name_not_letters), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'MCA 106 should only have letters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_location_not_letters(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.location_not_letters), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Marurui 106 should only have letters')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
        
    def test_office_name_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_name_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'No field should be a space')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_type_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_type_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'No field should be a space')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_location_space(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.location_space), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "No field should be a space")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_name_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_name_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Ensure no field is blank')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_type_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office_type_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Ensure no field is blank')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_location_blank(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.location_blank), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "Ensure no field is blank")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_president_location_not_kenya(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.president_location_not_kenya), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "The location of an executive office can only be Kenya")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_prime_min_location_not_kenya(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.prime_min_location_not_kenya), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], "The location of an executive office can only be Kenya")
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_less_keys(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/parties', data=json.dumps(self.office_less_keys), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Check if all fields exist')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_invalid_office_type(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.invalid_office_type), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Office type must either be Legislative, Executive or County')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_president(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_president), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or ' \
                        'a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_prime_minister(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_prime_minister), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or ' \
                        'a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_legislative_mismatch_governor(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_governor), content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or ' \
                        'a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_legislative_mismatch_mca(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.legislative_mismatch_mca), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Senator, Member of Parliament or ' \
                        'a Women Rep can occupy a legislative office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_governor(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_governor), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or ' \
                        'the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_senator(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_senator), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or '\
                        'the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_mp(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_mp), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only the President or the Prime Minister can occupy an executive office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_executive_mismatch_women_rep(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.executive_mismatch_women_rep), 
                                    content_type='application/json', headers=token)
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
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_president), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_prime_minister(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_prime_minister), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_senator(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_senator), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_county_mismatch_mp(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_mp), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)

    def test_county_mismatch_women_rep(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.county_mismatch_women_rep), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Only a Governor or an MCA can occupy a county office')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
    def test_office_exists(self):
        token = self.admin_token()
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.post('/api/v2/offices', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office already exists')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('data' in result)
    
class TestNotFoundCase(BaseTest):
    
    def test_get_specific_office_invalid_id(self):
        """Test GET specific party invalid id request"""
        user_token = self.user_token()
        response = self.client.get('/api/v2/offices/106', data=json.dumps(self.office), 
                                    content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)
    
    def test_delete_specific_office_invalid_id(self):
        """Test DELETE specific office invalid id request"""
        token = self.admin_token()
        response = self.client.delete('/api/v2/offices/106', data=json.dumps(self.office), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        self.assertEqual(result['Error'], 'Political office cannot be found')
        self.assertEqual(response.status_code, 404)
        self.assertFalse('data' in result)