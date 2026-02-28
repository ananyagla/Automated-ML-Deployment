import os
import importlib
import joblib

MODEL_FOLDER = "models"

def train_all_models():
    for file in os.listdir(MODEL_FOLDER):
        if file.endswith(".py"):
            module_name = file.replace(".py", "")
            module = importlib.import_module(f"models.{module_name}")

            if hasattr(module, "train"):
                print(f"Training {module_name}...")
                model = module.train()
                joblib.dump(model, f"models/{module_name}.pkl")

    print("All models trained successfully.")

if __name__ == "__main__":
    train_all_models()