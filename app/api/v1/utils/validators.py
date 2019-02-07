import re

class Validators:
    
    types_of_offices = ['Legislative', 'Executive', 'County']
    office_names = ['President','Prime Minister' 'Governor', 'Senator', 'Member of Parliament', 'Women Rep', 'MCA']

    def party_data_validator(self, party_name, hqAddress, logoUrl):
        response = True
        if not isinstance(party_name, str):
            response = {'Error': 'The name of the political party should be in string format'}

        if not isinstance(hqAddress, str):
            response =  {'Error': 'The party headquarters should be in string format'}
        
        if not re.search('[A-Za-z]', hqAddress):
            response = {'Error': 'HQ Address must have letters'} 
        
        if len(party_name) < 3:
            response = {'Error' : 'Party name too short'}
        
        if len(hqAddress) < 3:
            response = {'Error' : 'HQ Address too short'}
        
        if len(logoUrl) < 3:
            response = {'Error' : 'Logo URL too short'}

        return response

    def office_data_validator(self, office_type, name):
        response = True
        if not isinstance(office_type, str):
            response = {'Error': 'Office type should be in string format'}

        if not isinstance(name, str):
            response =  {'Error': 'Office name should be in string format'}
        
        if  office_type not in self.types_of_offices:
            response = {'Error': 'Office type must either be Legislative, Executive or County'}
            
        if office_type == 'Legislative':
            if name != 'Member of Parliament' and name != 'Women Rep':
                response = {'Error': 'Only a Member of Parliament or a Women Rep can occupy a legislative office'} 
        
        if office_type == 'Executive':
            if name != 'President' and name != 'Prime Minister':
                response = {'Error': 'Only the Presient can occupy an executive office'} 

        if office_type == 'County':
            if name != 'Governor' and name != 'MCA':
                response = {'Error': 'Only a Governor or a Women Rep can occupy a county'} 

        return response    