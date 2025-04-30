import pandas as pd
import os
import numpy as np
from wine_quality_predictor import logger
from sklearn.model_selection import train_test_split
from wine_quality_predictor.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # ===== Outlier Removal and Normalization =====
        df = data.copy()
        features = ['residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'alcohol']

        for feature in features:
            Q1 = df[feature].quantile(0.25)
            Q3 = df[feature].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            df = df[(df[feature] >= lower) & (df[feature] <= upper)]

            # Min-max normalization
            minimum = df[feature].min()
            maximum = df[feature].max()
            df[feature] = (df[feature] - minimum) / (maximum - minimum)

        # Log transform a skewed feature
        df['free sulfur dioxide'] = np.log1p(df['free sulfur dioxide'])

       
        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(df)



        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted, cleaned, and oversampled data into training and test sets.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print("Train:", train.shape)
        print("Test:", test.shape)

    