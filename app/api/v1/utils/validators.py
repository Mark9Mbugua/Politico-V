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