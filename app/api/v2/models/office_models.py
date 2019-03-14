from app.db_config import init_db
from psycopg2.extras import RealDictCursor
import psycopg2

class PoliticalOffices():
    def __init__(self):
        self.db = init_db()
        self.cur = self.db.cursor(cursor_factory=RealDictCursor)

    def create_office(self, office_name, office_type, location):
        query = """INSERT INTO offices(office_name, office_type, location)
                VALUES (%s,%s, %s) RETURNING office_id, office_name, office_type, location"""
        content = (office_name, office_type, location)
        self.cur.execute(query, content)
        office = self.cur.fetchone()
        self.db.commit()
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
        self.db.commit()
        self.cur.close()
