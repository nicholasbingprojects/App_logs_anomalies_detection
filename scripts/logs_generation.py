import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters for synthetic data generation
num_records = 1000  # Total number of log entries
num_anomalies = 50  # Number of anomalous entries
user_ids = [f'user_{i}' for i in range(1, 21)]  # 20 unique users
actions = ['login', 'file_upload', 'file_delete']
statuses = ['success', 'failure']

# Generate timestamps
start_time = datetime.now() - timedelta(days=30)  # Start from 30 days ago
timestamps = [start_time + timedelta(minutes=i) for i in range(num_records)]

# Generate synthetic log data
data = []
for i in range(num_records):
    user_id = np.random.choice(user_ids)
    action = np.random.choice(actions)
    status = np.random.choice(statuses)
    
    # Randomly generate duration
    duration = np.random.randint(200, 5000)  # Between 200 ms and 5000 ms
    error_code = np.nan if status == 'success' else np.random.randint(400, 500)  # Error codes for failures
    
    # Create anomaly condition
    anomaly = 1 if i < num_anomalies else 0  # First 'num_anomalies' are anomalous
    
    data.append([timestamps[i], user_id, action, status, duration, error_code, anomaly])

# Create a DataFrame
log_df = pd.DataFrame(data, columns=['Timestamp', 'UserID', 'Action', 'Status', 'Duration', 'ErrorCode', 'anomaly'])

# Shuffle the DataFrame to mix anomalous entries with normal ones
log_df = log_df.sample(frac=1).reset_index(drop=True)

# Save to CSV
log_df.to_csv('data/logs.csv', index=False)

print("Synthetic log data generated and saved as 'logs.csv'.")