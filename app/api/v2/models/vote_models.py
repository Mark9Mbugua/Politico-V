from app.db_config import init_db
from psycopg2.extras import RealDictCursor
import itertools

class Vote():
    def __init__(self):
        self.db = init_db()
        self.cur = self.db.cursor(cursor_factory=RealDictCursor)
    
    def cast_vote(self, office, voter, candidate):
        """Cast vote"""
        query = """INSERT INTO votes(office, voter, candidate)
                VALUES (%s,%s,%s) RETURNING office, voter, candidate"""
        content = (office, voter, candidate)
        self.cur.execute(query, content)
        vote = self.cur.fetchone()
        self.db.commit()
        return vote
    

    def has_voted(self,office, voter):
        self.cur.execute("""SELECT * FROM votes WHERE office = {} and voter = {}""".format(office, voter))
        vote_cast = self.cur.fetchall()
        return vote_cast
    
    def results_per_office(self, office):
        cur = self.db.cursor()
        query = """SELECT candidate, COUNT (vote_id) FROM votes WHERE office = {} GROUP BY candidate """.format(office)
        cur.execute(query, office)
        votes = cur.fetchall()

        data =[]
        keys = ('office', 'candidate', 'result')

        if votes:
            for vote in votes:
                vote = (office, ) + vote
                result = dict(zip(keys, vote))
                data.append(result)
        
            return data
        

        
