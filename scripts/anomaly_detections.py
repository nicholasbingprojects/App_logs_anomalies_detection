import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

class AnomalyDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        """Train the anomaly detection model."""
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """Predict anomalies in the test set."""
        return self.model.predict(X_test)

    def evaluate(self, y_test, y_pred):
        """Evaluate model performance."""
        return classification_report(y_test, y_pred)