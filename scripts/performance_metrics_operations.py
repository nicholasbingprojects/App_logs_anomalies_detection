from database.db_config import MongoDB
import pandas as pd

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

    def close(self):
        self.db.close()