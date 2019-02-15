from pymongo import MongoClient
client = MongoClient()

db = client.test
employee = db.employee

import pandas as pd
data = pd.read_csv('hrdata.csv')

































