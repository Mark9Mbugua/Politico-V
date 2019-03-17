from tests.v2.base_test import BaseTest
import json

class TestNormalVoteCase(BaseTest):
    def test_get_election_result(self):
        """Test GET the total votes for a particular candidate"""
        token = self.admin_token()
        user_token = self.user_token()
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(self.register), 
                                    content_type='application/json', headers=token)
        result = json.loads(response.data)
        response = self.client.post('/api/v2/vote', data=json.dumps(self.vote), 
                                    content_type='application/json', headers=user_token)
        result = json.loads(response.data)
        response = self.client.get('/api/v2/office/1/result', headers=user_token)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Election results retrieved successfully')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in result)