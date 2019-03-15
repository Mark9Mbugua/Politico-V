from app.db_config import Database
from psycopg2.extras import RealDictCursor
import psycopg2

class PoliticalOffices(Database):
    def __init__(self):
        super().__init__()

    def create_office(self, office_name, office_type, location):
        query = """INSERT INTO offices(office_name, office_type, location)
                VALUES (%s,%s, %s) RETURNING office_id, office_name, office_type, location"""
        content = (office_name, office_type, location)
        self.cur.execute(query, content)
        office = self.cur.fetchone()
        self.connect.commit()
        self.cur.close()
        return office
    
    def check_office_exists_by_name(self, office_name, location):
        self.cur.execute("""SELECT * FROM offices WHERE office_name= '{}' and location = '{}'""".format(office_name, location))
        office = self.cur.fetchall()
        return office

    def get_all_offices(self):
        self.cur.execute("SELECT * from offices")
        office_list = self.cur.fetchall()
        return office_list

    def get_one_office(self, office_id): 
        self.cur.execute("""SELECT * FROM offices WHERE office_id = {}""".format(office_id))
        office = self.cur.fetchone()
        return office
    
    def delete_office(self, office_id):
        self.cur.execute("""DELETE FROM offices WHERE office_id = '{}'""".format(office_id))
        self.connect.commit()
        self.cur.close()
