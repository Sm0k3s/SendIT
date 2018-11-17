"""module for parcel model that persists data into the db"""
from datetime import datetime
from .database import Database as db

db.initialize("dbname='sendit' user='postgres' password='smokes' host='localhost'")

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
        self.price = int(self.weight * 2)
        self.current_location = self.pickup_location
        self.status = status
        self.sent_on = sent_on

    def save_to_db(self):
        """saves a parcel to the database"""
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

    @classmethod
    def cancel_a_parcel(cls, id):
        """cancels the parcel with the id provided"""
        query = """UPDATE parcels SET status = %s WHERE id = %s"""
        tup =('canceled' , id)
        db.insert(query, tup)

    @classmethod
    def change_current_location(cls, location, id):
        """takes location provided and replaces the current one"""
        query = """UPDATE parcels SET status = %s WHERE id = %s"""
        tup =(location , id)
        db.insert(query, tup)

# p=ParcelModel('cakes','tasty cakes', 'eldoret','nairobi',9,1)
# p.save_to_db()
# ParcelModel.cancel_a_parcel(1)
