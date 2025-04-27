import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
num_records = 100000
start_time = datetime(2025, 4, 24)

# log levels and event types
log_levels = ['INFO', 'WARNING', 'ERROR']
event_types = ['LOGIN', 'LOGOUT', 'DATA_PROCESSING']
users = [f'user_{str(i).zfill(3)}' for i in range(1, 21)]  # 20 users
locations = ["New York, USA", "Suva, Fiji", "Port Moresby, PNG", "Lae, PNG", "Sydney, Australia"]

# Generate log entries
data = []
for i in range(num_records):
    timestamp = start_time + timedelta(seconds=i * 10)
    log_level = random.choice(log_levels)
    event_type = random.choice(event_types)
    user_id = random.choice(users)
    status_code = random.choice([200, 401, 404, 500]) if log_level != 'INFO' else 200
    response_time = random.randint(50, 1000)  # Random response time in ms
    location = random.choice(locations)
    
    message = f"{event_type} event for {user_id}"
    
    # Specific messages for ERROR and WARNING
    if log_level == 'ERROR':
        message = f"Error occurred: {message}"
    elif log_level == 'WARNING':
        message = f"Warning: {message}"

    data.append([timestamp, log_level, event_type, user_id, message, status_code, response_time, location])

# Create DataFrame
df = pd.DataFrame(data, columns=['timestamp', 'log_level', 'event_type', 'user_id', 'message', 'status_code', 'response_time', 'location'])

# Save to CSV
df.to_csv('logs.csv', index=False)