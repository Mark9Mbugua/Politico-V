from urllib.parse import urlparse
import re

class Validators:
    types_of_offices = ['Legislative', 'Executive', 'County']
    
    def is_alpha_or_space(self, data):
        for x in data:
            if x.isalpha() or x.isspace():
                return  True
            return False
    
    def is_space(self, data):
        if re.search(r'\s', data):
            return True
        return False 
    
    def is_empty(self, data):        
        if data.isspace() or data == "":
            return True
        return False
    
    def is_digit(self, data):
        for x in data:
            if x.isdigit():
                return True
            return False
    
    def is_str(self, data):
        if isinstance(data, str):
            return True
        return False

    def valid_office_type(self, office_type, types_of_offices):
        if office_type in self.types_of_offices:
            return True
        return False

    def valid_legilative_office(self, office_type, office_name): 
        if office_type == 'Legislative':
            if 'Member of Parliament' in office_name  and 'Women Rep' in office_name and 'Senator' in office_name:
                return True
            return False

    def valid_executive_office(self, office_type, office_name):     
        if office_type == 'Executive':
            if office_name == "President" or office_name == 'Prime Minister':
                return True
            return False
    
    def valid_executive_location(self, office_type, location):
        if office_type == 'Executive':
            if location == 'Kenya':
                return True
            return False
   
    def valid_county_office(self, office_type, office_name):
        if office_type == 'County':
            if 'Governor' in office_name  or 'MCA' in office_name:
                return True
            return False
    
    def password_short(self, data):
        """ validates user password """
        if len(data) < 8:
            return True
        return False
    
    def caps_password(self, data):
        if not re.search('[A-Z]', data):
            return True
        return False

    def small_letter_password(self, data):
        if not re.search('[a-z]', data):
            return True
        return False
    
    def integer_password(self, data):
        if not re.search('[0-9]', data):
            return True
        return False
    
    def valid_email(self, email):
        valid = re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip())
        if not valid:
            return False
        return True
    
    def short_phone_no(self, data):
        if len(data) != 12:
            return True
        return False
    
    """Validate logoUrl"""
    def valid_logo_url(self, data):
        parsed_url = urlparse(data)
        if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
            return True
        return False



