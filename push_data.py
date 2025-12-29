import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtrace():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)

            records = list(json.loads(data.T.to_json( )).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=certifi.where()
                )
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]   #MongoClient  →  Database  →  Collection  →  Documents

            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "onkarai"
    collection = "NetworkData"
    network_obj = NetworkDataExtrace()
    records = network_obj.csv_to_json_convertor(FILE_PATH)
    len_of_records= network_obj.insert_data_mongodb(records,DATABASE,collection)
    print(len_of_records)