from kfp.dsl import component, Input, Output, Dataset, Model, Metrics
import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

@component(
    base_image="python:3.9",
    packages_to_install=["pandas", "scikit-learn", "joblib"]
)
def evaluate_model_component(
    model_input: Input[Model],
    test_data: Input[Dataset],
    metrics_output: Output[Metrics]
):
    # Load test data
    df = pd.read_csv(test_data.path)
    X_test = df.drop("target", axis=1)
    y_test = df["target"]

    # Load trained model
    model = joblib.load(model_input.path)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate accuracy
    acc = accuracy_score(y_test, y_pred)

    # Log metrics
    metrics_output.log_metric("accuracy", float(acc))
    print(f"Model Accuracy: {acc}")

