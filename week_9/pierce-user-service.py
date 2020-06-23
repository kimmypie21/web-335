#Title: Assignment 9.2
#Author: Kimberly Pierce
#Date: 22 June 2020
#Modified By: Kimberly Pierce
#Description: Assignment 9.2 Querying and Creating Documents

import pymongo.mongo_client
import pprint
import datetime
client = pymongo.MongoClient('localhost', 27017)
db= client.web335
print(client)



user={
    "first_name":"Dolly",
    "last_name": "Parton",
    "email": "dparton@dollywood.com",
    "employee_id": "Dolly",
    "date_created": datetime.datetime.utcnow()
}

user_id=db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id":"Dolly"}))