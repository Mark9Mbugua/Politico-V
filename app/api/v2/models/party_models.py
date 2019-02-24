from app.db_config import init_db
import psycopg2
import itertools

class PoliticalParties():
    def __init__(self):
        self.db = init_db()
    
    #serializes data into json object format
    
    def serializer(self, party):
        party_fields = ('party_id', 'party_name', 'hqAddress', 'logoUrl')
        result = dict()
        for index, field in enumerate(party_fields):
            result[field] = party[index]
        return result
    
    def serializer_two(self, party_details):
        party_id, party_name, hqAddress, logoUrl = party_details
        result = dict(party_id=party_id, party_name=party_name, hqAddress=hqAddress, logoUrl=logoUrl)
        return result

    def create(self, party_name, hqAddress, logoUrl):
        cur = self.db.cursor()
        query = """INSERT INTO parties(party_name, hqAddress, logoUrl)
                VALUES (%s,%s,%s) RETURNING party_id"""
        content = (party_name, hqAddress, logoUrl)
        cur.execute(query, content)
        party_id = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(party_id, content)))
    
    def check_party_exists(self, party_id):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM parties WHERE party_id= '{}'""".format(party_id))
        party = cur.fetchall()
        return party

    
    def get_all_parties(self):
        cur = self.db.cursor()
        query = """SELECT party_id, party_name, hqAddress, logoUrl FROM parties"""
        columns = ('party_id', 'party_name', 'hqAddress', 'logoUrl')
        cur.execute(query)
        party_details = cur.fetchall()
        if party_details:
            parties = []
            for detail in party_details:
                party_values = []
                for value in detail:
                    party_values.append(str(value))
                parties.append(dict(zip(columns, party_values)))
            return parties
        return None


    def get_one_party(self, party_id):
        cur = self.db.cursor()
        query = """SELECT * FROM parties WHERE party_id = {}""".format(party_id, )
        cur.execute(query)
        party = cur.fetchone()
        cur.close()
        if party:
            return self.serializer_two(party)
        return None
    
    def edit_party(self, party_id, party_name):
        cur = self.db.cursor()
        query = """UPDATE parties SET party_name = '{}' WHERE party_id = '{}' RETURNING party_name""".format(party_name, party_id)
        cur.execute(query)
        self.db.commit()
        name = cur.fetchone()
        cur.close()
        if name:
            name_change = name
            new_name = dict(name_change=name_change)
            return new_name
        return None
    
    def delete_party(self, party_id):
        cur = self.db.cursor()
        query = """DELETE FROM parties WHERE party_id = '{}'""".format(party_id, )
        cur.execute(query)
        self.db.commit()
        cur.close()
        return None

