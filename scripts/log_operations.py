from database.db_config import MongoDB
import pandas as pd
import requests

class LogDB:
    def __init__(self):
        self.db = MongoDB(db_name='log_database')
        self.collection = self.db.get_collection('logs')
        self.db.create_indexes('logs')

    def insert_logs(self, log_data):
        """Insert log data into the database."""
        if isinstance(log_data, pd.DataFrame):
            records = log_data.to_dict(orient='records')
            self.collection.insert_many(records)
        else:
            raise ValueError("log_data must be a DataFrame.")

    def get_latest_logs(self, limit=100):
        """Retrieve the latest logs."""
        return pd.DataFrame(list(self.collection.find().sort('_id', -1).limit(limit)))

    def get_anomalies(self):
        """Retrieve detected anomalies."""
        return pd.DataFrame(list(self.collection.find({"anomaly": -1})))

    def aggregate_metrics(self):
        """Aggregate metrics for analysis."""
        pipeline = [
            {
                "$group": {
                    "_id": "$metric1",
                    "average_metric2": {"$avg": "$metric2"},
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {"count": -1}
            }
        ]
        return pd.DataFrame(list(self.collection.aggregate(pipeline)))

    def complex_query(self, start_date, end_date):
        """Retrieve logs within a date range with specific conditions."""
        query = {
            "timestamp": {"$gte": start_date, "$lte": end_date},
            "anomaly": {"$ne": 1}  # Exclude anomalies
        }
        return pd.DataFrame(list(self.collection.find(query)))

    def collect_logs_from_web_server(self, url):
        """Collect logs from a web server API."""
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())  # Assume the response is in JSON format

    def collect_logs_from_application_service(self, service_url):
        """Collect logs from an application service."""
        response = requests.get(service_url)
        response.raise_for_status()
        return pd.DataFrame(response.json())

    def collect_logs_from_database(self, db_name, collection_name, query={}):
        """Collect logs from a MongoDB database."""
        db_collection = self.db.get_collection(collection_name, db_name)
        return pd.DataFrame(list(db_collection.find(query)))

    def close(self):
        self.db.close()