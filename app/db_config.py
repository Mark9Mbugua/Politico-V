import psycopg2
import os

db_url = 'postgresql://postgres:1998@localhost:5432/politico_db'
test_db_url = 'postgresql://postgres:1998@localhost:5432/test_politico_db'

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
                user_id SERIAL PRIMARY KEY NOT NULL,
                firstname VARCHAR(80) NOT NULL,
                lastname VARCHAR(80) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone INTEGER NOT NULL UNIQUE,
                password VARCHAR NOT NULL,
                role VARCHAR(80) NOT NULL DEFAULT 'User',
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
                candidate INTEGER NOT NULL,
                office INTEGER NOT NULL,
                party INTEGER NOT NULL,
                email VARCHAR(100) NOT NULL,
                PRIMARY KEY (candidate, office))"""

        votes = """CREATE TABLE IF NOT EXISTS votes(
                office INTEGER NOT NULL,
                candidate INTEGER NOT NULL,
                voter INTEGER NOT NULL,
                PRIMARY KEY (office, voter))"""

        queries = [users, offices, parties, candidates, votes]
        return queries
