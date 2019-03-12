from app.api.v2.utils.serializer import Serializer
from app.db_config import init_db
from flask_jwt_extended import create_access_token
from .office_models import PoliticalOffices
from .party_models import PoliticalParties
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor
import itertools

class User():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        user_fields = ('user_id', 'firstname','lastname','username', 'email', 'phone', 'password')
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
    
    def register(self, firstname, lastname, username, email, phone, password):
        """Create a user account"""
        cur = self.db.cursor()
        query = """INSERT INTO users(firstname, lastname, username, email, phone, password)
                VALUES (%s,%s,%s,%s,%s,%s) RETURNING user_id"""
        content = (firstname, lastname, username, email, phone, password)
        cur.execute(query, content)
        user = cur.fetchone()
        self.db.commit()
        cur.close() 
        return self.serializer(tuple(itertools.chain(user, content)))
    
    def login(self, username, password):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, firstname, lastname, username, email, password, phone FROM users WHERE username = '{}'""".format(username))
        user= cur.fetchone()
        if cur.rowcount == 1: 
            data = self.serializer(user)
            if self.generate_hash(password):
                return data
                
    def get_user_by_username(self, username):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM users WHERE username = '{}'""".format(username))
        user = cur.fetchall()
        return user
    
    def get_user_by_id(self, username):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id FROM users WHERE username ='{}'""".format(username))
        user_id = cur.fetchone()
        return user_id
    
    def email_exists(self, email):
        cur = self.db.cursor()
        cur.execute("SELECT email from users WHERE email = '{}'".format(email))
        data = cur.fetchone()
        email = data[0]
        return email
    
    def userIsValid(self, username):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, firstname, lastname, username, email, password FROM users WHERE username= %s""", (username, ))
        data = cur.fetchall()
        for user in data:
            if user[3] == username:
                return True
    
    def password_is_valid(self, username, password):
        """Check if password is correct"""
        cur = self.db.cursor()
        cur.execute("""SELECT password FROM users WHERE username = %s""", (username, ))
        data = cur.fetchone()
        passcode = self.serializer_two(data)
        if self.verify_hash(password, passcode["pwd"]) is  True:
            return True
    
    def get_password(self, username):
        cur = self.db.cursor()
        cur.execute("""SELECT password FROM users WHERE username = '{}'""".format(username))
        data = cur.fetchone()
        if data:
            password = data.get('password')
        return password

    def generate_token(self, username):
        user_id = self.get_user_by_id(username)
        token = create_access_token(identity=user_id)
        return token

    def user_login(self, username):
        token = self.generate_token(username)
        return token
    
    def create_admin(self):
        pwd = self.generate_hash('Marksman001')
        if self.get_user_by_username('admin'):
            return 'Admin already exists'
        self.register('Mark', 'Mbugua', 'admin', 'mimini@admin.com', '0712340908', pwd)
        self.promote_user_to_admin()
    
    def promote_user_to_admin(self):
        cur =self.db.cursor()
        cur.execute("UPDATE users SET is_admin = 'true' where username = 'admin'")
        self.db.commit()
    
    def get_admin_by_id(self, user_id):
        cur =self.db.cursor()
        cur.execute("""SELECT * from users WHERE user_id = {} and username = 'admin'""".format(user_id))
        admin = cur.fetchall()
        return admin  
    
    def i_am_admin(self, user_id):
        for u_id in user_id:
            if u_id:
                cur =self.db.cursor()
                cur.execute("SELECT * from users WHERE user_id = {} and is_admin = 'true'".format(u_id))
                user = cur.fetchall()
                self.promote_user_to_admin()
                return user
    
    def find_by_user_id(self, user_id):
        cur =self.db.cursor()
        cur.execute("SELECT * from users WHERE user_id = {}".format(user_id))
        user = cur.fetchall()
        return user

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """returns True if password has been hashed"""
        return sha256.verify(password, hash)


