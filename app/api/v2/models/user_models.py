from app.db_config import init_db
from .party_models import PoliticalParties
from .office_models import PoliticalOffices
import itertools
from passlib.hash import pbkdf2_sha256 as sha256
from app.api.v2.utils.serializer import Serializer


class User():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        user_fields = ('user_id', 'firstname','lastname', 'email', 'phone', 'password', 'role')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def candidate_serializer(self, user):
        user_fields = ('office', 'candidate', 'email')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def serializer_two(self, password):
        (pwd ,) = password
        result = dict(pwd=pwd)

        return result
    
    def third_serializer(self, user_details):
        user_id, firstname, lastname, email, phone, password = user_details
        result = dict(user_id = user_id, firstname = firstname, lastname = lastname, email = email, phone = phone,  password = password)

        return result
    
    def register(self, firstname, lastname, email, phone, password, role):
        """Create a user account"""
        cur = self.db.cursor()
        query = """INSERT INTO users(firstname, lastname, email, phone, password, role)
                VALUES (%s,%s,%s,%s,%s,%s) RETURNING user_id"""
        content = (firstname, lastname, email, phone, password, role)
        cur.execute(query, content)
        user = cur.fetchone()
        self.db.commit()
        cur.close() 
        return self.serializer(tuple(itertools.chain(user, content)))
    
    def login(self, email, password):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, firstname, lastname, email, password, phone, role FROM users WHERE email = %s""", (email, ))
        user= cur.fetchone()
        if cur.rowcount == 1: 
            data = self.serializer(user)
            if self.generate_hash(password):
                return data
                

    def userIsValid(self, email):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, firstname, lastname, email, password FROM users WHERE email= %s""", (email, ))
        data = cur.fetchall()
        for user in data:
            if user[3] == email:
                return True
    
    def password_is_valid(self, email, password):
        """Check if password is correct"""
        cur = self.db.cursor()
        cur.execute("""SELECT password FROM users WHERE email = %s""", (email, ))
        data = cur.fetchone()
        passcode = self.serializer_two(data)
        if self.verify_hash(password, passcode["pwd"]) is  True:
            return True
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """returns True if password has been hashed"""
        return sha256.verify(password, hash)

class Candidate(User):
    def register_candidate(self, office, party, email, candidate):
        if self.userIsValid(email) == True:
            try:
                cur = self.db.cursor()
                query = """INSERT INTO candidates(office, party, email, candidate)
                        VALUES (%s,%s,%s, %s) RETURNING office, party, email, candidate"""
                content = (office, party, email, candidate)
                cur.execute(query, content)
                user = cur.fetchone()
                self.db.commit()
                cur.close()
                return self.candidate_serializer(tuple(itertools.chain(user, content)))
            except Exception as error:
                print(error)
        raise Exception('A candidate must be a registered user first')

    def check_candidate_registered(self, candidate, office):
        cur = self.db.cursor()
        cur.execute( """SELECT * FROM candidates WHERE candidate = %s and office = %s""", (candidate, office))
        candidate = cur.fetchone()
        return candidate


