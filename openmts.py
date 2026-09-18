import joblib
import sklearn
import cv2
import os
os.environ["KERAS_BACKEND"] = "torch"
import keras
import torch
import numpy as np

class ModelDownloader:
    def __init__(self, model_type, tier):
        self.model_type = model_type
        self.tier = tier

    def _download_model(self, file_name, url):
        from tqdm import tqdm
        import urllib.request


        with tqdm(unit='B', unit_scale=True, desc=file_name) as bar:
            def update(block_num, block_size, total_size):
                if bar.total is None:
                    bar.total = total_size
                bar.update(block_size)

            if not os.path.exists(f"models/{file_name}"):
                try:
                    urllib.request.urlretrieve(url, f"models/{file_name}", reporthook=update)
                except Exception as e:
                    raise RuntimeError(f"Failed to download {file_name}: {e}")

    def download_model(self):

        os.makedirs("models", exist_ok=True)

        match self.model_type:
            case "gender_pred":
                match self.tier:
                    case "nano":
                        self._download_model("gender-model-nano.joblib", "https://github.com/yasin2343jaberynsar/OpenMTS/releases/download/gender_pred_update/gender-model-nano.joblib")
                    case "baseline":
                        self._download_model("gender-model-baseline.keras", "https://github.com/yasin2343jaberynsar/OpenMTS/releases/download/gender_pred_update/gender-model-baseline.keras")
                    case "plus":
                        self._download_model("gender-model-plus.keras", "https://github.com/yasin2343jaberynsar/OpenMTS/releases/download/gender_pred_update/gender-model-plus.keras")
                        

class GenderPredModel():
    def __init__(self, tier : str):
        models = ["nano", "baseline", "plus"]
        if not tier in models:
            raise ValueError(f"Model {tier} not found")
        self.tier = tier
        model = ModelDownloader("gender_pred", tier)
        model.download_model()
        if tier == "nano":
            self.model = joblib.load(f"models/gender-model-{tier}.joblib")
        else:
            self.model = keras.models.load_model(f"models/gender-model-{tier}.keras")

    def predict(self, X):

        if self.tier != "nano":
            X = cv2.resize(X, (128, 128))
            X = np.array([X])

            pred = self.model.predict(X, verbose=0)
            if pred[0][0] > pred[0][1]:
                pred = "Male"
            else:
                pred = "Female"

            return pred

        else:
            X = cv2.resize(X, (64, 64))
            X = X.reshape(1, 64*64*3)

            pred = self.model.predict(X)

            if pred == 0:
                pred = "Male"
            else:
                pred = "Female"

            return pred
