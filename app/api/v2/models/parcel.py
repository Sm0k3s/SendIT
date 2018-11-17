"""module for parcel model that persists data into the db"""
from datetime import datetime
from database import Database as db

class ParcelModel():
    """model to persist parcel information into the database"""

    def __init__(self, title, description, destination, pickup_location,weight,
                 sender_id,price="", current_location="",
                 status='in transit', sent_on=datetime.now().__str__()):
        self.title = title
        self.description = description
        self.destination = destination
        self.pickup_location = pickup_location
        self.weight = weight
        self.sender_id = sender_id
        self.price = price
        self.current_location = current_location
        self.status = status
        self.sent_on = sent_on

    def save_to_db(self):
        query = """INSERT INTO parcels(title, description,destination,
                   pickup_location,weight,sender_id, price,
                   current_location, status, sent_on)
                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
        tup = (self.title, self.description, self.destination, self.pickup_location,
               self.weight, self.sender_id, self.price, self.current_location,
               self.status, self.sent_on)
        db.insert(query, tup)

    @classmethod
    def find_by_id(cls,id):
        """Finds a parcel by its id"""
        query = "SELECT * FROM parcels WHERE id=%s"
        return db.find_one(query, (id,))

    @classmethod
    def find_by_sender_id(cls,sender_id):
        """Finds a parcel by its senders id"""
        query = "SELECT * FROM parcels WHERE id=%s"
        return db.find_one(query, (sender_id,))
