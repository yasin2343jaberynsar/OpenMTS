import joblib
import sklearn
import cv2

class GenderPredModel():
    def __init__(self, tier : str):
        models = ["nano", "baseline", "plus"]
        if not tier in models:
            raise ValueError(f"Model {tier} not found")
        self.model = joblib.load(f"models/gender-model-{tier}.joblib")

    def predict(self, X):

        X = cv2.resize(X, (64, 64))
        X = X.reshape(1, 64*64*3)
        pred = self.model.predict(X)
        if pred == 0:
            pred = "Male"
        else:
            pred = "Female"

        return pred

    def retrain(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def save(self, filename):
        joblib.dump(self.model, f"{filename}.joblib")