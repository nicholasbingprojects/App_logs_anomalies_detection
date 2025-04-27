import unittest
import logging
from scripts.logging_setup import setup_logging

class TestLoggingSetup(unittest.TestCase):
    def test_logging_setup(self):
        setup_logging('logs/test.log')
        logging.info("This is a test log.")
        
        with open('logs/test.log', 'r') as log_file:
            logs = log_file.readlines()
            self.assertTrue(any("This is a test log." in line for line in logs))

if __name__ == "__main__":
    unittest.main()