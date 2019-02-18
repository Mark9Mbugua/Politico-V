from app.db_config import init_db
import itertools



class Vote():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, vote):
        vote_fields = ('office_id', 'office_name', 'candidate_id','candidate_firstname','candidate_lastname', 'voter_id')
        result = dict()
        for index, field in enumerate(vote_fields):
            result[field] = vote[index]
        return result
    
    def third_serializer(self, user_details):
        user_id, firstname, lastname, email, phone, password = user_details
        result = dict(user_id = user_id, firstname = firstname, lastname = lastname, email = email, phone = phone,  password = password)

        return result
    
    def cast_vote(self, office_name, candidate_id, cd_firstname, cd_lastname, voter_id):
        """Cast vote"""
        cur = self.db.cursor()
        query = """INSERT INTO votes(office_name, candidate_id, cd_firstname, cd_lastname, voter_id)
                VALUES (%s,%s,%s,%s,%s) RETURNING office_id"""
        content = (office_name, candidate_id, cd_firstname, cd_lastname, voter_id)
        cur.execute(query, content)
        vote = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(vote, content)))