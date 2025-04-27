import unittest
import pandas as pd
from scripts.anomaly_detections import AnomalyDB

class TestAnomalyDetection(unittest.TestCase):

    def setUp(self):
        # Create an instance of AnomalyDB
        self.anomaly_db = AnomalyDB()

        # Create a sample DataFrame for testing
        self.log_data = pd.DataFrame({
            'timestamp': pd.date_range(start='2025-04-24', periods=10, freq='S'),
            'metric1': [1, 2, 1.5, 10, 1, 1, 1, 1, 1, 1],
            'metric2': [5, 5, 5, 5, 5, 5, 5, 5, 5, 100]  # Anomaly in last entry
        })

    def test_detect_anomalies(self):
        anomalies = self.anomaly_db.detect_anomalies(self.log_data)
        self.assertGreater(len(anomalies), 0, "Anomalies should be detected.")

    def tearDown(self):
        self.anomaly_db.close()

if __name__ == '__main__':
    unittest.main()