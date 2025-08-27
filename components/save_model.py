import argparse
import shutil

def save_model(model_path: str, output_path: str):
    """Save model artifact to output path"""
    shutil.copy(model_path, output_path)
    print(f"✅ Model copied to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--output-path", type=str, required=True)
    args = parser.parse_args()

    save_model(args.model_path, args.output_path)
