import unittest
import os
import json
import psycopg2
from app import create_app
from flask import jsonify
from .dummy_data import dummy_data
from app.db_config import Database
from app.api.v2.models.user_models import User

class BaseTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            Database().destroy_table()
            Database().create_tables()
            User().create_admin()
        self.user_sign_up = dummy_data['user_sign_up']
        self.admin_sign_in = dummy_data['admin_sign_in']
        self.user_sign_in = dummy_data['user_sign_in']
        self.wrong_password = dummy_data['wrong_password']
        self.user_not_exist = dummy_data['user_not_exist']
        self.office = dummy_data['office']
        self.office_less_keys = dummy_data['office_less_keys']
        self.office_name_blank = dummy_data['office_name_blank']
        self.office_type_blank = dummy_data['office_type_blank']
        self.location_blank = dummy_data['location_blank']
        self.office_name_space = dummy_data['office_name_space']
        self.office_type_space = dummy_data['office_type_space']
        self.location_space = dummy_data['location_space']
        self.invalid_office_type = dummy_data['invalid_office_type']
        self.president_location_not_kenya = dummy_data['president_location_not_kenya']
        self.prime_min_location_not_kenya = dummy_data['prime_min_location_not_kenya']
        self.office_type_not_string = dummy_data['office_type_not_string']
        self.office_name_not_string = dummy_data['office_name_not_string']
        self.location_not_string = dummy_data['location_not_string']
        self.office_type_not_letters =  dummy_data['office_type_not_letters']
        self.office_name_not_letters = dummy_data['office_name_not_letters']
        self.location_not_letters = dummy_data['location_not_letters']
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
        self.party = dummy_data['party']
        self.same_party = dummy_data['same_party']
        self.party_less_keys = dummy_data['party_less_keys']
        self.edit_party_no_name_key = dummy_data['edit_party_no_name_key']
        self.hq_add_not_spaces_int_str = dummy_data['hq_add_not_spaces_int_str']
        self.hq_add_no_str = dummy_data['hq_add_no_str']
        self.party_name_blank = dummy_data['party_name_blank']
        self.hqAddress_blank = dummy_data['hqAddress_blank']
        self.logoUrl_blank = dummy_data['logoUrl_blank']
        self.party_name_space = dummy_data['party_name_space']
        self.hqAddress_space = dummy_data['hqAddress_space']
        self.logoUrl_space = dummy_data['logoUrl_space'] 
        self.logoUrl_no_scheme = dummy_data['logoUrl_no_scheme']
        self.logoUrl_no_netloc = dummy_data['logoUrl_no_netloc']
        self.logoUrl_no_path = dummy_data['logoUrl_no_path']
        self.party_name_not_purely_alpha_and_space = dummy_data['party_name_not_purely_alpha_and_space']
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
        self.phone_short = dummy_data['phone_short']
        self.firstname_not_string = dummy_data['firstname_not_string']
        self.lastname_not_string = dummy_data['lastname_not_string']
        self.username_not_string = dummy_data['username_not_string']
        self.email_not_string = dummy_data['email_not_string']
        self.phone_not_string = dummy_data['phone_not_string']
        self.password_not_string = dummy_data['password_not_string']
        self.register = dummy_data['register']
        self.vote = dummy_data['vote']
       

    def user_registration(self):
        """ Register a user"""
        response = self.client.post('/api/v2/auth/signup',data = json.dumps(self.user_sign_up), 
                                    content_type= 'application/json')
        return response

    def admin_login(self):
        """Sign in Admin"""
        response = self.client.post('/api/v2/auth/signin',data = json.dumps(self.admin_sign_in), 
                                    content_type= 'application/json')
        return response
    
    def user_login(self):
        """Sign in a User"""
        response = self.client.post('/api/v2/auth/signin',data = json.dumps(self.user_sign_in), 
                                    content_type= 'application/json')
        return response

    def admin_token(self):
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
    
    def tearDown(self):
        with self.app.app_context():
            Database().create_tables()