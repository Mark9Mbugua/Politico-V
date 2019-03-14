from app.db_config import init_db
from psycopg2.extras import RealDictCursor


class Candidate():
    def __init__(self):
        self.db = init_db()
        self.cur = self.db.cursor(cursor_factory=RealDictCursor)

    def register_candidate(self, office, party, candidate):
        query = """INSERT INTO candidates(office, party, candidate)
                VALUES (%s,%s,%s) RETURNING office, party, candidate"""
        content = (office, party, candidate)
        self.cur.execute(query, content)
        candidate = self.cur.fetchone()
        self.db.commit()
        return candidate

    def check_candidate_registered(self, candidate, office):
        self.cur.execute( """SELECT * FROM candidates WHERE candidate = %s and office = %s""", (candidate, office))
        candidate = self.cur.fetchone()
        return candidate
    