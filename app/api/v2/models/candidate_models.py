from app.db_config import Database
from psycopg2.extras import RealDictCursor


class Candidate(Database):
    def __init__(self):
        super().__init__()

    def register_candidate(self, office, party, candidate):
        query = """INSERT INTO candidates(office, party, candidate)
                VALUES (%s,%s,%s) RETURNING office, party, candidate"""
        content = (office, party, candidate)
        self.cur.execute(query, content)
        candidate = self.cur.fetchone()
        self.connect.commit()
        return candidate

    def check_candidate_registered(self, candidate, office):
        self.cur.execute( """SELECT * FROM candidates WHERE candidate = %s and office = %s""", (candidate, office))
        candidate = self.cur.fetchone()
        return candidate
    