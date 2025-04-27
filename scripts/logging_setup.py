import logging
import random
import time

def setup_logging(log_file='logs/application.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        
    )
    logging.info("Logging setup complete.")

if __name__ == "__main__":
    setup_logging()