"""Module for the database model"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    """
    Database model
    """
    @classmethod
    def initialize(cls, uri):
        """Method to start the connection with the database"""
        cls.conn = psycopg2.connect(uri)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def create_all(cls):
        """Creates all tables"""
        cls.cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            firstname VARCHAR(255),
            surname VARCHAR(255),
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255),
            role VARCHAR(255),
            joined_on TIMESTAMP DEFAULT NOW()
            );
            CREATE TABLE IF NOT EXISTS parcels(
                id serial PRIMARY KEY,
                title VARCHAR(255),
                description VARCHAR(255),
                destination VARCHAR(255),
                pickup_location VARCHAR(255),
                weight INTEGER,
                price VARCHAR(255),
                status VARCHAR(255) DEFAULT 'in-transit',
                sent_on TIMESTAMP DEFAULT NOW(),
                current_location VARCHAR(255),
                sender_id INTEGER REFERENCES users(id)
                )""")
        cls.conn.commit()

    @classmethod
    def insert(cls, query, tup):
        """Will be used with insert statements"""
        cls.cur.execute(query, tup)
        cls.conn.commit()

    @classmethod
    def find_one(cls, query, tup):
        """Returns the first result in a query"""
        cls.cur.execute(query, tup)
        return cls.cur.fetchone()

    @classmethod
    def find_many(cls, query, tup):
        """Returns all the results in a query"""
        cls.cur.execute(query, tup)
        return cls.cur.fetchall()

    @classmethod
    def drop_all(cls):
        """Drops all tables"""
        cls.cur.execute("""DROP TABLE IF EXISTS users CASCADE;
                        DROP TABLE IF EXISTS parcels CASCADE;""")
        cls.conn.commit()
