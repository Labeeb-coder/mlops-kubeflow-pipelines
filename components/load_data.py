from sklearn.datasets import load_iris
import pandas as pd
from kfp.v2.dsl import component, Output, Dataset

@component
def load_data_component(output_csv: Output[Dataset]):
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Save dataset to output path
    df.to_csv(output_csv.path, index=False)

