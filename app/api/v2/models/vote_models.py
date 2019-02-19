from app.db_config import init_db
import itertools

class Vote():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, vote):
        vote_fields = ('office_id', 'candidate_id', 'voter_id')
        result = dict()
        for index, field in enumerate(vote_fields):
            result[field] = vote[index]
        return result
    
    def cast_vote(self, office_id, candidate_id, voter_id):
        """Cast vote"""
        cur = self.db.cursor()
        query = """INSERT INTO votes(office, cast_by, candidate)
                VALUES (%s,%s,%s) RETURNING cast_by, candidate"""
        content = (office_id, voter_id, candidate_id)
        cur.execute(query, content)
        vote = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(vote, content)))
    

    def has_voted(self,office_id, cast_by):
        cur = self.db.cursor()
        query = """ SELECT EXISTS (SELECT * FROM votes WHERE office = %s and cast_by = %s)""".format(office_id, cast_by)
        content = (office_id, cast_by)
        cur.exectute(query, content)
        vote_cast = cur.fetchone()
        return vote_cast[0]