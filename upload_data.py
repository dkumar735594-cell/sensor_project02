from pymongo.mongo_clientpi import MongoClient
import pandas as pd
import json

#URL
uri = "mongodb+srv://deepak:jxeZCCcGS0NgkH0o@cluster0.wysnwqc.mongodb.net/?appName=Cluster0"

#create a new client and connect to server 
client = MongoClient(uri)

#create databasee name name and collection name 
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\Users\deepa\Downloads\sensor project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0", axis=1)

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)