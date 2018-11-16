"""Module for the database model"""
import psycopg2
from psycopg2.extras import RealDictCursor


class Database():
    """
    Database model
    """
    @staticmethod
    def initialize():
        """Method to start the connection with the database"""
        conn = psycopg2.connect(app.config['DATABASE_URI'])
        cur = conn.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def create_all():
        """creates all tables"""
        pass

    def drop_all():
        """drops all tables"""
        pass
