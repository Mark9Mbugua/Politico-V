from app.db_config import init_db
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor

class User():
    def __init__(self):
        self.db = init_db()
        self.cur = self.db.cursor(cursor_factory=RealDictCursor)
    
    def register(self, firstname, lastname, username, email, phone, password):
        """Create a user account"""
        query = """INSERT INTO users(firstname, lastname, username, email, phone, password)
                VALUES (%s,%s,%s,%s,%s,%s) RETURNING user_id, firstname, lastname, username, email, phone, password"""
        content = (firstname, lastname, username, email, phone, password)
        self.cur.execute(query, content)
        user = self.cur.fetchone()
        self.db.commit()
        return user

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
        self.cur.execute("UPDATE users SET is_admin = 'true' where username = 'admin'")
        self.db.commit()
    
    def get_admin_by_id(self, user_id):
        self.cur.execute("""SELECT * from users WHERE user_id = {} and username = 'admin'""".format(user_id))
        admin = self.cur.fetchall()
        return admin  
    
    def i_am_admin(self, user_id):
        self.cur.execute("SELECT * from users WHERE user_id = {} and is_admin = 'true'".format(user_id["user_id"]))
        user = self.cur.fetchall()
        self.promote_user_to_admin()
        return user
    
    def find_by_user_id(self, user_id):
        self.cur.execute("SELECT * from users WHERE user_id = {}".format(user_id))
        user = self.cur.fetchall()
        return user
    
    def get_user_by_username(self, username):
        self.cur.execute("""SELECT * FROM users WHERE username = '{}'""".format(username))
        user = self.cur.fetchall()
        return user
    
    def get_user_by_id(self, username):
        self.cur.execute("""SELECT user_id FROM users WHERE username ='{}'""".format(username))
        user_id = self.cur.fetchone()
        return user_id
    
    def email_exists(self, email):
        self.cur.execute("SELECT email from users WHERE email = '{}'".format(email))
        data = self.cur.fetchone()
        email = data[0]
        return email
    
    def userIsValid(self, username):
        self.cur.execute("""SELECT user_id, firstname, lastname, username, email, password FROM users WHERE username= %s""", (username, ))
        data = self.cur.fetchall()
        for user in data:
            if user[3] == username:
                return True
    
    def password_is_valid(self, username, password):
        """Check if password is correct"""
        self.cur.execute("""SELECT password FROM users WHERE username = %s""", (username, ))
        data = self.cur.fetchone()
        if self.verify_hash(password, data["password"]):
            return True
        return False
    
    def get_password(self, username):
        self.cur.execute("""SELECT password FROM users WHERE username = '{}'""".format(username))
        data = self.cur.fetchone()
        if data:
            password = data.get('password')
        return password

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """returns True if password has been hashed"""
        return sha256.verify(password, hash)


