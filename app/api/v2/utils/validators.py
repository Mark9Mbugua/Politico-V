from flask import abort, request
from app.api.v2.utils.serializer import Serializer
from urllib.parse import urlparse
import re

class Validators:
    types_of_offices = ['Legislative', 'Executive', 'County']
    
    def is_alpha_or_space(self, *args):
        for arg in args:
            for x in arg:
                if not x.isalpha() and not x.isspace():
                    abort(Serializer.error_fn(400, '{} should only have letters and spaces'.format(arg)))
    
    def has_space(self, *args):
        for arg in args:
            if re.search(r'\s', arg):
                abort(Serializer.error_fn(400, '{} should not have spaces'.format(arg))) 
    
    def is_space_or_empty(self, *args, **kwargs):
        for arg in args:        
            if arg.isspace():
                abort(Serializer.error_fn(400, 'No field should be a space'))
        
        for value in kwargs.values():
            if value == "":
                abort(Serializer.error_fn(400, 'Ensure no field is blank'))
  
    def is_str_or_int(self, *args):
        for arg in args:
            if not isinstance(arg, str):
               abort(Serializer.error_fn(400, 'All fields should be in string format'))
            if isinstance(arg, int):
                abort(Serializer.error_fn(400, 'All fields should be in string format'))

    def is_digit(self, *args):
        for arg in args:    
            for x in arg:
                if x.isdigit():
                    abort(Serializer.error_fn(400, '{} should only have letters'.format(arg)))

    def all_digits(self, *args):
        for arg in args:    
            if arg.isdigit():
                abort(Serializer.error_fn(400, '{} should have letters too'.format(arg)))
    
    def is_digit_or_letter(self, *args):
        for arg in args:    
            for x in arg:
                if not x.isalpha() and not x.isdigit() and not x.isspace():
                    abort(Serializer.error_fn(400, '{} should have letters. '\
                         'It may also have digits and spaces'.format(arg)))
    
    def is_int(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                abort(Serializer.error_fn(400, '{} should be a number'.format(arg)))
 
    def is_not_digit(self, *args):
        for arg in args:    
            if not arg.isdigit():
                abort(Serializer.error_fn(400, '{} should only have digits'.format(arg)))

    def valid_office_type(self, office_type, types_of_offices):
        if office_type not in self.types_of_offices:
           abort(Serializer.error_fn(400, 'Office type must either be Legislative, Executive or County'))

    def valid_legilative_office(self, office_type, office_name): 
        if office_type == 'Legislative':
            if 'Member of Parliament' not in office_name  and 'Women Rep' not in office_name and 'Senator' not in office_name:
                abort(Serializer.error_fn(400, "Only a Senator, Member of Parliament "\
                    "or a Women Rep can occupy a legislative office"))

    def valid_executive_office(self, office_type, office_name):     
        if office_type == 'Executive':
            if office_name != "President" and office_name != 'Prime Minister':
                abort(Serializer.error_fn(400, "Only the President or the Prime Minister "\
                    "can occupy an executive office"))
    
    def valid_executive_location(self, office_type, location):
        if office_type == 'Executive':
            if location != 'Kenya':
                abort(Serializer.error_fn(400, 'The location of an executive office can only be Kenya'))
   
    def valid_county_office(self, office_type, office_name):
        if office_type == 'County':
            if 'Governor' not in office_name  and 'MCA' not in office_name:
                abort(Serializer.error_fn(400, "Only a Governor or an MCA "\
                    "can occupy a county office"))
    
    def check_valid_password(self, data):
        if len(data) < 8:
            abort(Serializer.error_fn(400, "Password should not be less than 8 characters"))    
       
        pwd_caps = re.search(r'[A-Z]', data)
        pwd_small = re.search(r'[a-z]', data)
        pwd_numbers = re.search(r'[0-9]', data)
        if not pwd_caps or not pwd_small or not pwd_numbers:
            abort(Serializer.error_fn(400,"Password should have at least one small letter, "\
                          "one capital letter and one number"))
    
    def valid_email(self, email):
        valid = re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip())
        if not valid:
            abort(Serializer.error_fn(400, "Email address is invalid. "\
            "Kindly enter a valid email address"))
    
    def valid_phone_number(self, phone):
        if len(phone) != 12:
            abort(Serializer.error_fn(400, "Phone number should have 12 digits " \
            "starting with the country code for example: 254712345678"))
    
    """Validate logoUrl"""
    def valid_logo_url(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc or not parsed_url.path:
            abort(Serializer.error_fn(400, "logoUrl should be in the example format "\
            "'https://www.twitter.com/profile/img.jpg'"))



