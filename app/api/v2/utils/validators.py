from passlib.hash import pbkdf2_sha256 as sha256
import re

class Validators:
    
    types_of_offices = ['Legislative', 'Executive', 'County']
    office_names = ['President','Prime Minister' 'Governor', 'Senator', 'Member of Parliament', 'Women Rep', 'MCA']

    def party_data_validator(self, party_name, hqAddress):
        response = True
        if not all(x.isalpha() or x.isspace() for x in party_name):
            response = {'Error': 'Name should only have letters and spaces', 'Status': 400}
        
        if not all(x.isdigit() or x.isalpha() or x.isspace() for x in hqAddress):
            response = {'Error': 'hqAddress should have letters, spaces and numbers only', 'Status': 400}
        
        if all(x.isdigit() for x in hqAddress):
            response = {'Error': 'hqAddress should have letters too', 'Status': 400}

        if not isinstance(party_name, str):
            response = {'Error': 'Name should be in string format', 'Status': 400}

        if not isinstance(hqAddress, str):
            response = {'Error': 'hqAddress should be in string format', 'Status': 400}
        
        if party_name == "" or party_name.isspace():
            response = {'Error': 'Party name is required', 'Status': 400}
        
        if hqAddress == "" or hqAddress.isspace():
            response = {'Error': 'hqAddress is required', 'Status': 400}
        
        return response

    def office_data_validator(self, office_type, name):
        response = True
        if not isinstance(office_type, str):
            response = {'Error': 'Office type should be in string format', 'Status': 400}
        if not isinstance(name, str):
            response =  {'Error': 'Office name should be in string format', 'Status': 400}
        
        if  office_type not in self.types_of_offices:
            response = {'Error': 'Office type must either be Legislative, Executive or County', 'Status': 400}
            
        if office_type == 'Legislative':
            if name != 'Member of Parliament' and name != 'Women Rep' and name != 'Senator':
                response = {'Error': 'Only a Senator, Member of Parliament or a Women Rep can occupy a legislative office', 'Status': 400} 
        
        if office_type == 'Executive':
            if name != 'President' and name != 'Prime Minister':
                response = {'Error': 'Only the President or the Prime Minister can occupy an executive office', 'Status': 400} 

        if office_type == 'County':
            if name != 'Governor' and name != 'MCA':
                response = {'Error': 'Only a Governor or an MCA can occupy a county office', 'Status': 400} 

        return response 
    
    def user_sign_up_validator(self, firstname, lastname, email, phone, password):
        """ validates user password """
        response = True
        if len(password) < 5:
            response = {'Error': 'Password should have at least 5 characters'}
            return response
        
        if not re.search('[A-Z]', password):
            response = {'Error': 'Password should have atleast one capital letter', 'Status': 404}
        
        if not re.search('[a-z]', password):
            response = {'Error': 'Password should have atleast one lowercase letter', 'Status': 404}
        
        if not re.search('[0-9]', password):
            response = {'Error': 'Password should have atleast one number'}, 404
        
        if not all(x.isalpha() or x.isspace() for x in firstname):
            response = {'Error': 'Username should only have letters and spaces', 'Status': 400}
        
        if not all(x.isalpha() or x.isspace() for x in firstname):
            response = {'Error': 'Username should only have letters and spaces', 'Status': 400}
        
        if re.search('@', email) is None:
            response = {'Error': "Email should be in the format 'name@address.com'", 'Status': 400}
        
        if not isinstance(firstname, str):
            response = {'Error': 'Name should be in string format', 'Status': 400}
        
        if not isinstance(lastname, str):
            response = {'Error': 'Name should be in string format', 'Status': 400}
        
        if not isinstance(email, str):
            response = {'Error': 'Email should be in string format', 'Status': 400}
        
        if len(email) < 7:
            response = {'Error': 'Email is too short', 'Status': 400}
        
        if not all(x.isdigit() for x in phone):
            response = {'Error': 'Phone number should have digits only', 'Status': 400}
        
        if len(phone) < 8:
            response = {'Error': 'Phone number should have at least 8 digits', 'Status': 400}

        
        return response
        
        

    

