import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src" / "wine_quality_predictor" / "pipeline"))

from wine_quality_predictor.pipeline.prediction import PredictionPipeline




def main():


    st.title("🍷 Wine Quality Predictor")
    st.write("This app predicts the quality of wine based on various features.")

    st.sidebar.header("Input Features")

    fixed_acidity = st.sidebar.number_input("Fixed Acidity", 0.0, 20.0, 10.0, 0.1)
    volatile_acidity = st.sidebar.number_input("Volatile Acidity", 0.0, 2.0, 0.5, 0.01)
    citric_acid = st.sidebar.number_input("Citric Acid", 0.0, 2.0, 0.3, 0.01)
    residual_sugar = st.sidebar.number_input("Residual Sugar", 0.0, 100.0, 20.0, 0.1)
    chlorides = st.sidebar.number_input("Chlorides", 0.0, 1.0, 0.05, 0.01)
    total_sulfur_dioxide = st.sidebar.number_input("Total Sulfur Dioxide", 0, 500, 100, 1)
    pH = st.sidebar.number_input("pH", 0.5, 5.0, 3.2, 0.01)
    sulphates = st.sidebar.number_input("Sulphates", 0.3, 5.0, 1.5, 0.01)
    alcohol = st.sidebar.number_input("Alcohol", 8.0, 20.0, 10.5, 0.1)

    input_data = pd.DataFrame({
    'fixed acidity': [fixed_acidity],
    'volatile acidity': [volatile_acidity],
    'citric acid': [citric_acid],
    'residual sugar': [residual_sugar],
    'chlorides': [chlorides],
    'total sulfur dioxide': [total_sulfur_dioxide],
    'pH': [pH],
    'sulphates': [sulphates],
    'alcohol': [alcohol]
})

    if st.button("Predict"):
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(input_data)
        st.success(f"Predicted Wine Quality: {prediction[0]}")
    else:
        st.info("Enter features and click 'Predict' to see results.")

if __name__ == "__main__":
    main()
