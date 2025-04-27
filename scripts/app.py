import pandas as pd
from datetime import datetime
from log_operations import LogDB
from scripts.anomaly_detections import AnomalyDB
from performance_metrics_operations import PerformanceMetricsDB

def main():
    log_db = LogDB()
    anomaly_db = AnomalyDB()
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

    # Example: Inserting an anomaly
    anomaly_record = {
        "timestamp": pd.Timestamp.now(),
        "metric_id": "metric1",
        "value": 100,
        "description": "Anomaly detected in CPU usage.",
        "severity": "high",
        "resolved": False,
        "resolution_notes": ""
    }
    anomaly_db.insert_anomaly(anomaly_record)

    # Example: Getting anomalies
    anomalies = anomaly_db.get_anomalies()
    print("Detected Anomalies:\n", anomalies)

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

    # Clean up
    log_db.close()
    anomaly_db.close()
    performance_metrics_db.close()

if __name__ == "__main__":
    main()