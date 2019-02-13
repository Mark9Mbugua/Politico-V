import os
import psycopg2

db_url  =os.getenv('DATABASE_URL')

def create_tables():
    conn = connection(db_url)
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()

def drop_tables():
    conn = connection(db_url)
    cur = conn.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE;"
    offices = "DROP TABLE IF EXISTS offices CASCADE;"
    parties = "DROP TABLE IF EXISTS parties CASCADE;"
    queries = [users, offices, parties]
    for query in queries:
        cur.execute(query)
    conn.commit()

def connection(url):
    connect = psycopg2.connect(url)
    return connect

def tables():
    table1 = """CREATE TABLE IF NOT EXISTS users(
        user_id SEIRAL PRIMARY KEY,
        name varchar (50) NOT NULL,
        email varchar UNIQUE,
        password varchar (50) NOT NULL,
        role varchar)"""

    table2 = """CREATE TABLE IF NOT EXISTS parties(
            party_id SERIAL PRIMARY KEY,
            party_name varchar UNIQUE,
            logoUrl varchar (80) NOT NULL)"""
    
    table3 = """CREATE TABLE IF NOT EXISTS offices(
            office_id Serial PRIMARY KEY,
            name varchar (75) NOT NULL)"""
    
    queries = [table1, table2, table3]
    return queries