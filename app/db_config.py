import psycopg2
import os
from passlib.hash import pbkdf2_sha256 as sha256

db_url = os.getenv('DATABASE_URL')
test_db_url = os.getenv('TEST_DATABASE_URL')
prod_db_url = os.getenv('PROD_DATABASE_URL')

def connection(url):
    con = psycopg2.connect(url)
    return con

def init_db():
    """establish db connection and create tables"""
    con = connection(db_url)
    cur = con.cursor()
    queries = tables()
    for query in queries:
        cur.execute(query)
    con.commit()
    return con

def init_prod_db():
    """establish db connection and create tables"""
    con = connection(prod_db_url)
    cur = con.cursor()
    queries = tables()
    for query in queries:
        cur.execute(query)
    con.commit()
    return con

def init_test_db():
    """establish test_db connection and create tables"""
    con = connection(test_db_url)
    cur = con.cursor()
    queries = tables()
    for query in queries:
        cur.execute(query)
    con.commit()
    return con

def drop_tables():
    con = connection(db_url)
    cur = con.cursor()
    parties = """DROP TABLE IF EXISTS parties CASCADE"""
    offices = """DROP TABLE IF EXISTS offices CASCADE"""
    users = """DROP TABLE IF EXISTS users CASCADE"""
    votes = """DROP TABLE IF EXISTS votes CASCADE"""
    candidates = """DROP TABLE IF EXISTS votes CASCADE"""
    queries = [parties, offices, users, candidates, votes]

    for query in queries:
        cur.execute(query)
    con.commit()

def drop_test_tables():
    con = connection(test_db_url)
    cur = con.cursor()
    parties = """DROP TABLE IF EXISTS parties CASCADE"""
    offices = """DROP TABLE IF EXISTS offices CASCADE"""
    users = """DROP TABLE IF EXISTS users CASCADE"""
    votes = """DROP TABLE IF EXISTS votes CASCADE"""
    candidates = """DROP TABLE IF EXISTS votes CASCADE"""
    queries = [parties, offices, users, candidates, votes]

    for query in queries:
        cur.execute(query)
    con.commit()

def tables():
    
        users = """CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY NOT NULL,
                firstname VARCHAR(80) NOT NULL,
                lastname VARCHAR(80) NOT NULL,
                username VARCHAR(80) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone INTEGER NOT NULL,
                password VARCHAR NOT NULL,
                is_admin BOOLEAN DEFAULT FALSE,
                date_created timestamp with time zone DEFAULT ('now'::text)::date)"""

        offices = """CREATE TABLE IF NOT EXISTS offices (
                office_id SERIAL PRIMARY KEY NOT NULL,
                office_name VARCHAR(80) NOT NULL,
                office_type VARCHAR(80) NOT NULL)"""

        parties = """CREATE TABLE IF NOT EXISTS parties (
                party_id SERIAL PRIMARY KEY NOT NULL,
                party_name VARCHAR(80) NOT NULL,
                logoUrl VARCHAR(80) NOT NULL,
                hqAddress VARCHAR(80) NOT NULL)"""

        candidates = """CREATE TABLE IF NOT EXISTS candidates(
                candidate SERIAL NOT NULL,
                office INTEGER NOT NULL,
                party INTEGER NOT NULL,
                username VARCHAR(80) NOT NULL,
                PRIMARY KEY (candidate, office))"""

        votes = """CREATE TABLE IF NOT EXISTS votes(
                vote_id SERIAL NOT NULL,
                office INTEGER NOT NULL,
                voter INTEGER NOT NULL,
                candidate INTEGER NOT NULL,
                PRIMARY KEY (voter, office))"""

        queries = [users, offices, parties, candidates, votes]
        return queries