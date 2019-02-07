#storage structure for political parties is a list
parties = []

class PoliticalParties:
    def __init__(self):
        self.parties = parties
    
    def create_party(self, party_name, hqAddress, logoUrl):
        party = {}
        party['party_id'] = len(self.parties) + 1
        party['party_name'] = party_name
        party['hqAddress'] = hqAddress
        party['logoUrl'] = logoUrl

        self.parties.append(party)
        return party
    
    def get_all_parties(self):
        "Returns all parties"
        return parties
    
    def get_one_party(self, party_id):
        for party in self.parties:
            if party['party_id'] == party_id:
                return party
    
    def edit_party(self, party_id, party_name):
        for party in self.parties:
            if party['party_id'] == party_id:
                party['party_name'] = party_name
                return party