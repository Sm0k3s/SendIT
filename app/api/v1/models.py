from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    """
    A model for manipulating data for the users
    """
    Access = {
        2: 'admin',
        1 : 'user'
    }

    database = {}
    _id = 1

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    @classmethod
    def create_user(cls, username, email, password):
        user = {
            "id": cls._id,
            "username": username,
            "password": generate_password_hash(password),
            "email":email,
            "role": cls.Access[2]
        }
        cls.database[cls._id] = user
        cls._id += 1

class Parcel():
    """
    Model for parcels
    """
    state = {
        'cancel': 'canceled',
        'transit' : 'in transit'
    }
    database = {}
    _id = 1

    def __init__(self, destination, pickup_location,weight,
                 status=state['transit'], sent_on=datetime.now):
        self.destination = destination
        self.pickup_location = pickup_location
        self.weight = weight
        self.sent_on = sent_on
        self.status = status

    def create_parcel(self):
        parcel = {
            "id": Parcel._id,
            "destination": self.destination,
            "pickup_location": self.pickup_location,
            "weight":str(self.weight) + 'kg',
            "price": 'Kshs.' + str(self.weight *50),
            "status": self.status,
            'current_location': self.pickup_location
        }
        Parcel.database[Parcel._id] = parcel
        Parcel._id += 1

    @classmethod
    def cancel_parcel(cls, parcel_id):
        cls.database[parcel_id]['status'] = cls.state['cancel']

    def get_all():
        return Parcel.database

    @classmethod
    def search_by_key_value(cls, key, value):
        res = []
        for i in cls.database.values():
            if i[key] == value:
                res.append(i)
        return res
        
###################################
#         DEBUG PRINTS            #
# #################################
# Parcel('naks','msa',2).create_parcel()
# Parcel('nai','nax',1).create_parcel()
# Parcel('where','there',0.5).create_parcel()
# Parcel.cancel_parcel(1)
# Parcel.cancel_parcel(3)
# k = Parcel.search_by_key_value('destination', 'where')
# print(k)
# # print(Parcel.get_all())
# print(Parcel.database.keys())
# for key in Parcel.database.values():
#     res = []
#     if key['status'] == 'canceled':
#         res.append(key)
#     print(res)
