from app.db_config import init_db
import psycopg2
import itertools

class PoliticalOffices():
    def __init__(self):
        self.db = init_db()
    
    #serializes data into json object format
    def serializer(self, office):
        office_fields = ('office_id', 'office_name', 'office_type', 'location')
        result = dict()
        for index, field in enumerate(office_fields):
            result[field] = office[index]
        return result
    
    def serializer_two(self, office_details):
        office_id, office_name, office_type, location = office_details
        result = dict(office_id = office_id, office_name = office_name, office_type = office_type, location = location)
        return result
    
    def create_office(self, office_name, office_type, location):
        cur = self.db.cursor()
        query = """INSERT INTO offices(office_name, office_type, location)
                VALUES (%s,%s, %s) RETURNING office_id"""
        content = (office_name, office_type, location)
        cur.execute(query, content)
        office = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(office, content)))

    def check_office_exists(self, office_id):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM offices WHERE office_id= '{}'""".format(office_id))
        office = cur.fetchall()
        return office
    
    def check_office_exists_by_name(self, office_name, location):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM offices WHERE office_name= '{}' and location = '{}'""".format(office_name, location))
        office = cur.fetchall()
        return office

    def get_all_offices(self):
        cur = self.db.cursor()
        query = """SELECT office_id, office_name, office_type, location FROM offices"""
        columns = ('office_id', 'office_name', 'office_type', 'location')
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
    
    def edit_office(self, office_id, office_name):
        cur = self.db.cursor()
        query = """UPDATE offices SET office_name = '{}' WHERE office_id = '{}' RETURNING office_name""".format(office_name, office_id)
        cur.execute(query)
        self.db.commit()
        name = cur.fetchone()
        cur.close()
        if name:
            name_change = name
            new_name = dict(name_change=name_change)
            return new_name
        return None
    
    def delete_office(self, office_id):
        cur = self.db.cursor()
        query = """DELETE FROM offices WHERE office_id = '{}'""".format(office_id, )
        cur.execute(query)
        self.db.commit()
        cur.close()
        return None