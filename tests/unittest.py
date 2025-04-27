import pandas as pd
import unittest
from pymongo import MongoClient
from scripts.real_time_inference import get_latest_data, real_time_detection

class TestLogDetection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the MongoDB connection and create a test database."""
        cls.mongo_uri = "mongodb://localhost:27017"
        cls.client = MongoClient(cls.mongo_uri)
        cls.db = cls.client['test_log_database']
        cls.collection = cls.db['logs']

        # Create a sample log DataFrame for testing
        cls.log_data = {
            'timestamp': ['2025-04-24 08:00:00', '2025-04-24 08:05:12', '2025-04-24 08:15:45'],
            'log_level': ['INFO', 'ERROR', 'WARNING'],
            'event_type': ['LOGIN', 'DATA_PROCESSING', 'LOGOUT'],
            'user_id': ['user_001', 'user_002', 'user_001'],
            'message': ['User logged in', 'Error processing data', 'User logged out'],
            'status_code': [200, 500, 200],
            'response_time': [150, 300, 100],
            'location': ['New York, USA', 'Los Angeles, USA', 'New York, USA']
        }
        cls.df = pd.DataFrame(cls.log_data)
        cls.collection.insert_many(cls.df.to_dict('records'))  # Insert data into MongoDB

    def test_get_latest_data(self):
        # Simulate getting the latest data from MongoDB
        data = get_latest_data()  # Adjust function signature if needed
        self.assertGreater(len(data), 0, "There should be some data in the logs.")
        
        # Check for missing values in the DataFrame
        missing_values = data.isnull().sum().sum()
        self.assertEqual(missing_values, 0, "There should be no missing values.")

    def test_real_time_detection(self):
        # Simulate anomaly detection
        anomalies = real_time_detection()  # Adjust to return detected anomalies

        # Assuming you know the expected anomalies based on the test data
        expected_anomalies = self.df[self.df['log_level'] == 'ERROR']  # Adjust based on your logic
        self.assertTrue(not anomalies.empty, "Anomalies should be detected.")
        self.assertTrue(expected_anomalies.equals(anomalies), "Detected anomalies should match expected anomalies.")

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database."""
        cls.client.drop_database('test_log_database')  # Drop the test database
        cls.client.close()  # Close the MongoDB connection

if __name__ == '__main__':
    unittest.main()