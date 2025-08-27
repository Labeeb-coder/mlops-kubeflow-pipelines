from kfp import dsl
from components.load_data import load_data_component
from components.train_model import train_model_component
from components.evaluate_model import evaluate_model_component


@dsl.pipeline(
    name="mlops-demo-pipeline",
    description="A simple MLOps pipeline with data loading, training, and evaluation."
)
def my_pipeline():
    # Step 1: Load dataset
    load_task = load_data_component()

    # Step 2: Train model
    train_task = train_model_component(
        input_csv=load_task.outputs["output_csv"]
    )

    # Step 3: Evaluate model
    evaluate_model_component(
        model_input=train_task.outputs["model_output"],
        test_data=load_task.outputs["output_csv"]
    )


if __name__ == "__main__":
    from kfp import compiler
    compiler.Compiler().compile(
        pipeline_func=my_pipeline,
        package_path="my_pipeline.yaml"
    )

