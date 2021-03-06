
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
    

