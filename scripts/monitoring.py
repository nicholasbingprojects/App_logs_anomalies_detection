import logging
import time

def monitor_application():
    while True:
        logging.info("Application is running...")
        time.sleep(60)  # Log status every minute

if __name__ == "__main__":
    monitor_application()