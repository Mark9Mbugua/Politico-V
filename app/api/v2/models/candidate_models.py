from app.api.v2.utils.serializer import Serializer
from app.db_config import init_db
from flask_jwt_extended import create_access_token
from .office_models import PoliticalOffices
from .party_models import PoliticalParties
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor
import itertools


class Candidate():
    def __init__(self):
        self.db = init_db()
    
    def candidate_serializer(self, user):
        user_fields = ('reg_id', 'party', 'candidate', 'office')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def serializer_two(self, password):
        (pwd ,) = password
        result = dict(pwd=pwd)

        return result

    def register_candidate(self, office, party, candidate):
        cur = self.db.cursor()
        query = """INSERT INTO candidates(office, party, candidate)
                VALUES (%s,%s,%s) RETURNING office, party, candidate"""
        content = (office, party, candidate)
        cur.execute(query, content)
        user = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.candidate_serializer(tuple(itertools.chain(user, content)))

    def check_candidate_registered(self, candidate, office):
        cur = self.db.cursor()
        cur.execute( """SELECT * FROM candidates WHERE candidate = %s and office = %s""", (candidate, office))
        candidate = cur.fetchone()
        return candidate
    