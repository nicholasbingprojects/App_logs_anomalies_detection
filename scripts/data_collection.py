import requests
import pandas as pd

def collect_logs_from_web_server(url):
    """Collect logs from a web server API."""
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

def collect_logs_from_application_service(service_url):
    """Collect logs from an application service."""
    response = requests.get(service_url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

def collect_logs_from_database(mongo_client, db_name, collection_name, query={}):
    """Collect logs from a MongoDB database."""
    db_collection = mongo_client[db_name][collection_name]
    return pd.DataFrame(list(db_collection.find(query)))