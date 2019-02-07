#storage structure of offices is a list
offices = []

class PoliticalOffices:

    def __init__(self):
        self.offices = offices
    
    def create_office(self, office_type, name):
        office = {}
        office['office_id'] = len(offices) + 1
        office['office_type'] = office_type
        office['name'] = name

        self.offices.append(office)
        return office
