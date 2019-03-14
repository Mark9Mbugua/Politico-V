from app.db_config import init_db
from psycopg2.extras import RealDictCursor
import psycopg2


class PoliticalParties():
    def __init__(self):
        self.db = init_db()
        self.cur = self.db.cursor(cursor_factory=RealDictCursor)

    def create(self, party_name, hqAddress, logoUrl):
        query = """INSERT INTO parties(party_name, hqAddress, logoUrl)
                VALUES (%s,%s,%s) RETURNING party_id, party_name, hqAddress, logoUrl"""
        content = (party_name, hqAddress, logoUrl)
        self.cur.execute(query, content)
        self.db.commit()
        party = self.cur.fetchone()
        return party
    
    def check_party_exists_by_name(self, party_name):
        self.cur.execute("""SELECT * FROM parties WHERE party_name= '{}'""".format(party_name))
        party = self.cur.fetchall()
        return party
  
    def get_all_parties(self):
        self.cur.execute("SELECT * from parties")
        party_list = self.cur.fetchall()
        return party_list

    def get_one_party(self, party_id):
        self.cur.execute("""SELECT * FROM parties WHERE party_id = {}""".format(party_id))
        party = self.cur.fetchone()
        return party
    
    def edit_party(self, party_id, party_name):
        self.cur.execute(
            """UPDATE parties SET party_name = '{}' WHERE party_id = '{}' RETURNING party_name""".format(party_name, party_id)
            )
        self.db.commit()
        name = self.cur.fetchone()
        self.cur.close()
        return name
    
    def delete_party(self, party_id):
        self.cur.execute("""DELETE FROM parties WHERE party_id = '{}'""".format(party_id))
        self.db.commit()
        self.cur.close()

