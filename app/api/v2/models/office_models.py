from app.db_config import init_db
import psycopg2
import itertools

class PoliticalOffices():
    def __init__(self):
        self.db = init_db()
    
    #serializes data into json object format
    def serializer(self, office):
        office_fields = ('office_id', 'office_name', 'office_type')
        result = dict()
        for index, field in enumerate(office_fields):
            result[field] = office[index]
        return result
    
    def serializer_two(self, office_details):
        office_id, office_name, office_type = office_details
        result = dict(office_id = office_id, office_name = office_name, office_type = office_type)
        return result

    def create(self, office_name, office_type):
        cur = self.db.cursor()
        query = """INSERT INTO offices(office_name, office_type)
                VALUES (%s,%s) RETURNING office_id"""
        content = (office_name, office_type)
        cur.execute(query, content)
        office_id = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(office_id, content)))
    
    def get_all_offices(self):
        cur = self.db.cursor()
        query = """SELECT office_id, office_name, office_type FROM offices"""
        columns = ('office_id', 'office_name', 'office_type')
        cur.execute(query)
        office_details = cur.fetchall()
        if office_details:
            offices = []
            for detail in office_details:
                office_values = []
                for value in detail:
                    office_values.append(str(value))
                offices.append(dict(zip(columns, office_values)))
            return offices
        return None

    def get_one_office(self, office_id):
        cur = self.db.cursor()
        query = """SELECT * FROM offices WHERE office_id = {}""".format(office_id, )
        cur.execute(query)
        office = cur.fetchone()
        cur.close()
        if office:
            return self.serializer_two(office)
        return None