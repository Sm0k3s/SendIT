"""Module for the parcel model"""
from datetime import datetime
from .user import User

class Parcel():
    """
    Model for parcels
    """

    state = {'cancel': 'canceled', 'transit': 'in transit'}
    # database dict to store parcels
    database = {}
    _id = 1

    def __init__(self, destination, pickup_location, weight,
                 status=state['transit']):
        self.destination = destination
        self.pickup_location = pickup_location
        self.weight = weight
        self.status = status
        # self.sender_id = sender_id if len(User.database) <= 1 else len(User.database)

    def create_parcel(self):
        """Creates a new parcel and adds the time it was sent"""
        parcel = {
            "id": Parcel._id,
            "destination": self.destination,
            "pickup_location": self.pickup_location,
            "weight": str(self.weight) + 'grams',
            "price": 'Kshs.' + str(float(self.weight) * float(2)),
            "status": self.status,
            "sent_on": datetime.now().__str__(),
            "current_location": self.pickup_location,
            "sender_id": 1 if len(User.database) <= 1 else len(User.database)
        }
        Parcel.database[Parcel._id] = parcel
        Parcel._id += 1

    @classmethod
    def cancel_parcel(cls, parcel_id):
        """Cancels a parcel with the id provided"""
        cls.database[parcel_id]['status'] = cls.state['cancel']

    @classmethod
    def get_all(cls):
        """Returns all the parcels in the dict database"""
        return cls.database

    @classmethod
    def search_by_key_value(cls, key, value):
        """searches the dict database"""
        res = [i for i in cls.database.values() if i[key] == value]
        return res

    @classmethod
    def change_current_location(cls, parcel_id, location):
        """This method will only be available to the admin"""
        cls.database[parcel_id]['current_location'] = location

    # def get_parcel_by_userid(self,user_id):
    #

###################################
#         DEBUG PRINTS            #
# #################################
# Parcel('naks','msa',2).create_parcel()
# Parcel('nai','nax',1).create_parcel()
# Parcel('where','there',0.5).create_parcel()
# Parcel('where','over there',3).create_parcel()
# Parcel.cancel_parcel(1)
# Parcel.cancel_parcel(3)
# k = Parcel.search_by_key_value('destination', 'where')
# print(k)
# print(Parcel.get_all())
# print(Parcel.database.values())
# res = [i for i in Parcel.database.values() if i['destination'] == 'naks' and i['status'] == 'in transit']
# print('##')
# print(res)
# for key in Parcel.database.values():
#     res = []
#     if key['status'] == 'canceled':
#         res.append(key)
#     print(res)
