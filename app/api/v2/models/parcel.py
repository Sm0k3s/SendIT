"""module for parcel model that persists data into the db"""
from datetime import datetime
from .database import Database as db


class ParcelModel():
    """model to persist parcel information into the database"""

    def __init__(self, title, description, destination, pickup_location,weight,
                 sender_id, status='in transit',
                 sent_on=datetime.now().__str__()):
        self.title = title.title()
        self.description = description.title()
        self.destination = destination
        self.pickup_location = pickup_location
        self.weight = weight
        self.sender_id = sender_id
        self.price = int(self.weight) * 2
        self.current_location = self.pickup_location
        self.status = status
        self.sent_on = sent_on

    def save_to_db(self):
        self.sent_on = datetime.now().__str__()
        """saves a parcel to the database"""
        query = """INSERT INTO parcels(title, description,destination,
                   pickup_location,weight,sender_id, price,
                   current_location, status, sent_on)
                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
        tuple = (self.title, self.description, self.destination, self.pickup_location,
               self.weight, self.sender_id, self.price, self.current_location,
               self.status, self.sent_on)
        db.insert(query, tuple)

    @staticmethod
    def find_by_id(id):
        """Finds a parcel by its id"""
        query = "SELECT * FROM parcels WHERE id=%s"
        return db.find_one(query, (id,))

    @staticmethod
    def find_by_sender_id(sender_id):
        """Finds all parcels by its senders id"""
        query = "SELECT * FROM parcels WHERE sender_id=%s"
        return db.find_many(query, (sender_id,))

    @staticmethod
    def cancel_a_parcel(id):
        """cancels the parcel with the id provided"""
        query = """UPDATE parcels SET status = %s WHERE id = %s"""
        tuple =('canceled' , id)
        db.insert(query, tuple)

    @staticmethod
    def edit_a_parcel(destination, id):
        """edits a parcel's destination with the id provided"""
        query = """UPDATE parcels SET destination = %s WHERE id = %s"""
        tuple =(destination , id)
        db.insert(query, tuple)

    @staticmethod
    def change_current_location(location, id):
        """takes location provided and replaces the current one"""
        query = """UPDATE parcels SET current_location = %s WHERE id = %s"""
        tuple =(location , id)
        db.insert(query, tuple)

    @staticmethod
    def change_status(id):
        """changes the status of parcel to delivered"""
        query = """UPDATE parcels SET status = %s WHERE id = %s"""
        tuple =('delivered' , id)
        db.insert(query, tuple)

    @staticmethod
    def get_all_parcels():
        query = "SELECT * FROM parcels"
        return db.find_all(query)
