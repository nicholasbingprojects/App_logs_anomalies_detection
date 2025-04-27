import pandas as pd
from pymongo import MongoClient
from sklearn.ensemble import IsolationForest

# MongoDB connection
mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['log_database']
collection = db['logs']

def get_latest_data():
    """Fetch the latest 100 log entries from MongoDB."""
    try:
        data = list(collection.find().sort('_id', -1).limit(100))
        if not data:
            print("No data found in the collection.")
            return pd.DataFrame()  # Return an empty DataFrame if no data
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error fetching data from MongoDB: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def real_time_detection():
    """Detect anomalies in the latest log data."""
    latest_data = get_latest_data()
    
    if latest_data.empty:
        print("No data available for anomaly detection.")
        return

    # Check if required columns exist
    required_columns = ['metric1', 'metric2']
    if not all(col in latest_data.columns for col in required_columns):
        print(f"Missing columns in the data. Expected: {required_columns}")
        return

    model = IsolationForest(contamination=0.1)
    latest_data['anomaly'] = model.fit_predict(latest_data[required_columns])
    anomalies = latest_data[latest_data['anomaly'] == -1]
    
    if not anomalies.empty:
        print("Anomalies detected:")
        print(anomalies)
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    real_time_detection()