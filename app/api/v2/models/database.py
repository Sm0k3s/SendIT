"""Module for the database model"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    """
    Database model
    """
    @classmethod
    def initialize(cls):
        """Method to start the connection with the database"""
        cls.conn = psycopg2.connect(os.getenv("DATABASEURI"))
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def create_all(cls):
        """creates all tables"""
        cls.cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            firstname VARCHAR(255),
            surname VARCHAR(255),
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255)
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
    def drop_all():
        """drops all tables"""
        pass
