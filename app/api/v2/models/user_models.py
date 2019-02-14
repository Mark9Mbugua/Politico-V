from app.db_config import init_db
import itertools
from passlib.hash import pbkdf2_sha256 as sha256

class User():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        user_fields = ('user_id', 'username', 'email', 'password')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def register(self, username, email, password):
        """Create a user account"""
        cur = self.db.cursor()
        query = """INSERT INTO users(username, email, password)
                VALUES (%s,%s,%s) RETURNING user_id"""
        content = (username, email, password)
        cur.execute(query, content)
        user_id = cur.fetchone()
        self.db.commit()
        cur.close()
        output = self.serializer(tuple(itertools.chain(user_id, content)))
        return output

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        """returns True if password has been hashed"""
        return sha256.verify(password, hash)