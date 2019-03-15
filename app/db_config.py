import psycopg2
import os
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor

class Database:

        def __init__(self):
                self.connect_url = os.getenv('DATABASE_URL')
                self.connect = psycopg2.connect(self.connect_url)
                self.cur = self.connect.cursor(cursor_factory=RealDictCursor)


        def create_tables(self):
        
                users = """CREATE TABLE IF NOT EXISTS users(
                        user_id serial PRIMARY KEY NOT NULL,
                        firstname VARCHAR(80) NOT NULL,
                        lastname VARCHAR(80) NOT NULL,
                        username VARCHAR(80) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        phone BIGINT NOT NULL,
                        password VARCHAR NOT NULL,
                        is_admin BOOLEAN DEFAULT FALSE,
                        date_created timestamp with time zone DEFAULT ('now'::text)::date)"""

                offices = """CREATE TABLE IF NOT EXISTS offices (
                        office_id SERIAL PRIMARY KEY NOT NULL,
                        office_name VARCHAR(80) NOT NULL,
                        office_type VARCHAR(80) NOT NULL,
                        location VARCHAR(80) NOT NULL)"""

                parties = """CREATE TABLE IF NOT EXISTS parties (
                        party_id SERIAL PRIMARY KEY NOT NULL,
                        party_name VARCHAR(80) NOT NULL,
                        logoUrl VARCHAR(80) NOT NULL,
                        hqAddress VARCHAR(80) NOT NULL)"""

                candidates = """CREATE TABLE IF NOT EXISTS candidates(
                        reg_id SERIAL NOT NULL,
                        office INTEGER NOT NULL references offices(office_id) on delete cascade,
                        party INTEGER NOT NULL references parties(party_id) on delete cascade,
                        candidate INTEGER NOT NULL references users(user_id) on delete cascade,
                        PRIMARY KEY (candidate, office))"""

                votes = """CREATE TABLE IF NOT EXISTS votes(
                        vote_id SERIAL NOT NULL,
                        createdOn TIMESTAMP DEFAULT now(),
                        office INTEGER NOT NULL references offices(office_id) on delete cascade,
                        voter INTEGER NOT NULL references users(user_id) on delete cascade,
                        candidate INTEGER NOT NULL references users(user_id) on delete cascade,
                        PRIMARY KEY (voter, office))"""

                queries = [users, offices, parties, candidates, votes]
                
                try:
                        for query in queries:
                                if query:
                                        self.cur.execute(query)
                                self.connect.commit()
                except Exception as e:
                        return e
        
        def destroy_table(self):
                """Destroy tables"""
                users = "DROP TABLE IF EXISTS  users CASCADE"
                parties = "DROP TABLE IF EXISTS  parties CASCADE"
                offices = "DROP TABLE IF EXISTS  offices CASCADE"
                votes = "DROP TABLE IF EXISTS  voters CASCADE"
                candidates = "DROP TABLE IF EXISTS  candidates CASCADE"

                queries = [users, parties, offices, votes, candidates]
                
               
                for query in queries:
                        if query:
                                self.cur.execute(query)
                        self.connect.commit()