import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient

class LogDB:
    def __init__(self, mongo_uri="mongodb://localhost:27017", db_name="log_database", collection_name="logs"):
        """Initialize the database connection."""
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_anomalies(self):
        """Fetch anomalies from the database."""
        try:
            anomalies = pd.DataFrame(list(self.collection.find({"anomaly": True})))  # Adjust query as needed
            if anomalies.empty:
                print("No anomalies found in the database.")
            return anomalies
        except Exception as e:
            print(f"Error fetching anomalies: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def visualize_anomalies(self, anomalies):
        """Visualize anomalies with count and time series plots."""
        if anomalies.empty:
            print("No anomalies to visualize.")
            return

        # Count of Detected Anomalies by Type
        plt.figure(figsize=(12, 6))
        sns.countplot(data=anomalies, x='anomaly_type')  # Assuming 'anomaly_type' column exists
        plt.title('Count of Detected Anomalies by Type')
        plt.xticks(rotation=45)
        plt.ylabel('Count')
        plt.xlabel('Anomaly Type')
        plt.tight_layout()
        plt.show()

        # Time series of anomalies
        anomalies['timestamp'] = pd.to_datetime(anomalies['timestamp'])  # Assuming 'timestamp' column exists
        anomalies.set_index('timestamp', inplace=True)

        plt.figure(figsize=(12, 6))
        anomalies.resample('H').count()['anomaly_type'].plot()  # Resampling hourly
        plt.title('Anomalies Over Time')
        plt.ylabel('Count of Anomalies')
        plt.xlabel('Time')
        plt.tight_layout()
        plt.show()

    def close_connection(self):
        """Close the database connection."""
        self.client.close()

# Example usage
if __name__ == "__main__":
    log_db = LogDB()
    anomalies = log_db.get_anomalies()
    
    if not anomalies.empty:
        print(f"Detected anomalies:\n{anomalies}")
        log_db.visualize_anomalies(anomalies)
    else:
        print("No anomalies detected.")

    log_db.close_connection()