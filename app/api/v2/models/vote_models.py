from app.db_config import init_db
import itertools

class Vote():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, vote):
        vote_fields = ('vote_id','voter', 'candidate', 'office')
        result = dict()
        for index, field in enumerate(vote_fields):
            result[field] = vote[index]
        return result
    
    def cast_vote(self, office, voter, candidate):
        """Cast vote"""
        for voter_id in voter:
            if voter_id:
                cur = self.db.cursor()
                query = """INSERT INTO votes(office, voter, candidate)
                        VALUES (%s,%s,%s) RETURNING office, voter, candidate"""
                content = (office, voter_id, candidate)
                cur.execute(query, content)
                vote = cur.fetchone()
                self.db.commit()
                cur.close()
                return self.serializer(tuple(itertools.chain(vote, content)))
    

    def has_voted(self,office, voter):
         for voter_id in voter:
            if voter_id:
                cur = self.db.cursor()
                cur.execute("""SELECT * FROM votes WHERE office = {} and voter = {}""".format(office, voter_id))
                vote_cast = cur.fetchall()
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
        

        
