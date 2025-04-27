from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self, uri=None, db_name=None):
        self.client = MongoClient(uri or os.getenv('MONGO_URI'))
        self.db = self.client[db_name or os.getenv('DB_NAME')]
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

    def create_indexes(self, collection_name):
        collection = self.get_collection(collection_name)
        if collection_name == 'logs':
            collection.create_index([("timestamp", 1)])
            collection.create_index([("metric1", 1)])
            collection.create_index([("anomaly", 1)])
        elif collection_name == 'anomalies':
            collection.create_index([("timestamp", 1)])
            collection.create_index([("metric_id", 1)])
        elif collection_name == 'performance_metrics':
            collection.create_index([("metric_name", 1)])
            collection.create_index([("timestamp", 1)])

    def close(self):
        self.client.close()