import pandas as pd
from datetime import datetime, timedelta
from db_operations import LogDB, UserActivityDB, PerformanceMetricsDB

def main():
    log_db = LogDB()
    user_activity_db = UserActivityDB()
    performance_metrics_db = PerformanceMetricsDB()

    # Example: Inserting log data
    log_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=10, freq='H'),
        'metric1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'metric2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'anomaly': [0] * 10
    })
    log_db.insert_logs(log_data)

    # Example: Getting the latest logs
    latest_logs = log_db.get_latest_logs()
    print("Latest Logs:\n", latest_logs)

    # Example: Getting anomalies
    anomalies = log_db.get_anomalies()
    print("Detected Anomalies:\n", anomalies)

    # Example: Aggregating metrics
    metrics = log_db.aggregate_metrics()
    print("Aggregated Metrics:\n", metrics)

    # Example: Complex query for logs within a date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)
    filtered_logs = log_db.complex_query(start_date, end_date)
    print("Filtered Logs:\n", filtered_logs)

    # Example: Inserting user activity data
    user_activity_data = pd.DataFrame({
        'user_id': [1, 2, 1, 2],
        'action': ['login', 'logout', 'view', 'edit'],
        'timestamp': pd.date_range(start='2023-01-01', periods=4, freq='H')
    })
    user_activity_db.insert_activity(user_activity_data)

    # Example: Getting user activity logs
    activity_logs = user_activity_db.get_activity_logs()
    print("User Activity Logs:\n", activity_logs)

    # Example: Inserting performance metrics data
    performance_data = pd.DataFrame({
        'metric_name': ['CPU', 'Memory', 'Disk'],
        'value': [75, 60, 80],
        'timestamp': pd.date_range(start='2023-01-01', periods=3, freq='H')
    })
    performance_metrics_db.insert_metrics(performance_data)

    # Example: Getting performance metrics
    metrics_logs = performance_metrics_db.get_metrics()
    print("Performance Metrics Logs:\n", metrics_logs)

    log_db.close()
    user_activity_db.close()
    performance_metrics_db.close()

if __name__ == "__main__":
    main()