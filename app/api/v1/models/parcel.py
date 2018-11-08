from datetime import datetime

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
                 status=state['transit']):
        self.destination = destination
        self.pickup_location = pickup_location
        self.weight = weight
        #self.sent_on = sent_on
        self.status = status

    def create_parcel(self):
        parcel = {
            "id": Parcel._id,
            "destination": self.destination,
            "pickup_location": self.pickup_location,
            "weight":str(self.weight) + 'grams',
            "price": 'Kshs.' + str(float(self.weight) * float(2)),
            "status": self.status,
            "sent_on": datetime.now().__str__(),
            'current_location': self.pickup_location
        }
        Parcel.database[Parcel._id] = parcel
        Parcel._id += 1

    @classmethod
    def cancel_parcel(cls, parcel_id):
        cls.database[parcel_id]['status'] = cls.state['cancel']

    @classmethod
    def get_all(cls):
        return cls.database

    @classmethod
    def search_by_key_value(cls, key, value):
        res = [i for i in cls.database.values() if i[key] == value]
        return res

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
# print(Parcel.database.keys())
# for key in Parcel.database.values():
#     res = []
#     if key['status'] == 'canceled':
#         res.append(key)
#     print(res)
