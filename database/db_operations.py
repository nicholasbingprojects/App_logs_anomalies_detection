from db_config import MongoDB
import pandas as pd
from datetime import datetime

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

    def close(self):
        self.db.close()

# User Activity Operations
class UserActivityDB:
    def __init__(self):
        self.db = MongoDB(db_name='log_database')
        self.collection = self.db.get_collection('user_activity')
        self.db.create_indexes('user_activity')

    def insert_activity(self, activity_data):
        """Insert user activity data into the database."""
        if isinstance(activity_data, pd.DataFrame):
            records = activity_data.to_dict(orient='records')
            self.collection.insert_many(records)
        else:
            raise ValueError("activity_data must be a DataFrame.")

    def get_activity_logs(self):
        """Retrieve user activity logs."""
        return pd.DataFrame(list(self.collection.find()))

# Performance Metrics Operations
class PerformanceMetricsDB:
    def __init__(self):
        self.db = MongoDB(db_name='log_database')
        self.collection = self.db.get_collection('performance_metrics')
        self.db.create_indexes('performance_metrics')

    def insert_metrics(self, metrics_data):
        """Insert performance metrics data into the database."""
        if isinstance(metrics_data, pd.DataFrame):
            records = metrics_data.to_dict(orient='records')
            self.collection.insert_many(records)
        else:
            raise ValueError("metrics_data must be a DataFrame.")

    def get_metrics(self):
        """Retrieve performance metrics logs."""
        return pd.DataFrame(list(self.collection.find()))