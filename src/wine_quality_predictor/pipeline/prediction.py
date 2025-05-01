import joblib
import pandas as pd
import numpy as np
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)
        # Ensure the prediction stays in the range 1 to 10
        clipped_prediction = np.clip(prediction, 1, 10)
        return clipped_prediction