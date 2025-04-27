import os
import sys

# Set the path to the scripts directory
scripts_path = os.path.abspath('C:/Users/Nicholas Bing/Documents/App_logs_anomaly_detection/scripts')

# Add the scripts directory to the system path
sys.path.append(scripts_path)

# Launch Jupyter Notebook
os.system('jupyter notebook')