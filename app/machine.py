import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        prediction = self.model.predict(feature_basis)
        confidence = self.model.predict_proba(feature_basis).max(axis=1)
        return prediction[0], confidence[0]

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            joblib.dump((self.model, self.name, self.timestamp), f)

    @staticmethod
    def open(filepath):
        with open(filepath, 'rb') as f:
            model, name, timestamp = joblib.load(f)
        instance = Machine.__new__(Machine)
        instance.model = model
        instance.name = name
        instance.timestamp = timestamp
        return instance

    def info(self):
        return f"Base Model: {self.name}\n\nTimestamp: {self.timestamp}"
