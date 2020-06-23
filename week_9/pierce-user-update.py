#Title: Assignment 9.3
#Author: Kimberly Pierce
#Date: 22 June 2020
#Modified By: Kimberly Pierce
#Description: Assignment 9.3 Updating and Deleting Documents

import pymongo.mongo_client
import pprint
import datetime
client = pymongo.MongoClient('localhost', 27017)
db= client.web335
print(client)

db.users.update_one(
    {"employee_id":"Dolly"},
    {"$set": {"email": "pierce@my365.bellevue.edu"}}
)

pprint.pprint(db.users.find_one({"employee_id": "Dolly"}))