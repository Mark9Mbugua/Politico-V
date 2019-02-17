from app.db_config import init_db
import itertools

class Registration():
    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        reg_fields = ('user_id', 'office_id', 'firstname', 'lastname', 'email', 'office_name', 'office_type')
        result = dict()
        for index, field in enumerate(reg_fields):
            result[field] = user[index]
        return result
    
    def third_serializer(self, reg_details):
        user_id, office_id, firstname, lastname, email, office_name, office_type = reg_details
        result = dict(user_id = user_id, office_id = office_id,  firstname = firstname, lastname = lastname, email = email, office_name = office_name, office_type = office_type)

        return result
    
    def register_candidate(self, user_id, office_id, firstname, lastname, email, office_name, office_type):
        """Create candidate_registration"""
        cur = self.db.cursor()
        query = """INSERT INTO registration(user_id, office_id, firstname, lastname, email, office_name, office_type)
                VALUES (%s,%s,%s,%s,%s,%s, %s)"""
        content = (user_id, office_id, firstname, lastname, email, office_name, office_type)
        cur.execute(query, content)
        reg = cur.fetchone()
        self.db.commit()
        cur.close()
        output = self.serializer(tuple(itertools.chain(reg, content)))
        return output