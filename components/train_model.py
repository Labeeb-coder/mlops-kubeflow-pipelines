from kfp import dsl
from kfp.dsl import Input, Output, Dataset, Model
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


@dsl.component(base_image="python:3.9")
def train_model_component(input_csv: Input[Dataset], model_output: Output[Model]):
    """Train a simple Logistic Regression model."""
    df = pd.read_csv(input_csv.path)
    X = df.drop("target", axis=1)
    y = df["target"]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    joblib.dump(model, model_output.path)

