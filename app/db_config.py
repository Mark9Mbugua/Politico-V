import psycopg2
import os

db_url = os.getenv('DATABASE_URL')
test_db_url = os.getenv('TEST_DATABASE_URL')

def create_tables():
    conn = init_db()
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    conn.commit()

def create_test_tables():
    conn = test_init_db()
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    conn.commit()

def drop_tables():
    conn = connection(db_url)
    cur = conn.cursor()
    parties = """DROP TABLE IF EXISTS parties CASCADE"""
    offices = """DROP TABLE IF EXISTS offices CASCADE"""
    users = """DROP TABLE IF EXISTS users CASCADE"""
    queries = [parties, offices, users]

    for query in queries:
        cur.execute(query)
    conn.commit()

def drop_test_tables():
    conn = connection(test_db_url)
    cur = conn.cursor()
    parties = """DROP TABLE IF EXISTS parties CASCADE"""
    offices = """DROP TABLE IF EXISTS offices CASCADE"""
    users = """DROP TABLE IF EXISTS users CASCADE"""
    queries = [parties, offices, users]

    for query in queries:
        cur.execute(query)
    conn.commit()

def connection(url):
    connect = psycopg2.connect(url)
    return connect


def init_db():
    connect = connection(db_url)
    return connect

def test_init_db():
    connect = connection(test_db_url)
    return connect

def tables():
    
    table1 = """CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY NOT NULL,
                username VARCHAR(80) NOT NULL,
                email VARCHAR(80) NOT NULL UNIQUE,
                password VARCHAR NOT NULL,
                role VARCHAR(80) NOT NULL DEFAULT 'User',
                date_created timestamp with time zone DEFAULT ('now'::text)::date)"""


    table2 = """CREATE TABLE IF NOT EXISTS offices (
            office_id SERIAL PRIMARY KEY NOT NULL,
            office_name VARCHAR(80) NOT NULL,
            office_type VARCHAR(80) NOT NULL)"""

    table3 = """CREATE TABLE IF NOT EXISTS parties (
            party_id SERIAL PRIMARY KEY NOT NULL,
            party_name VARCHAR(80) NOT NULL,
            logoUrl VARCHAR(80) NOT NULL,
            hqAddress VARCHAR(80) NOT NULL)"""

    queries = [table1, table2, table3]
    return queries
