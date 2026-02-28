from fastapi import FastAPI
import joblib
import os

app = FastAPI()
models = {}

MODEL_FOLDER = "models"

@app.on_event("startup")
def load_models():
    for file in os.listdir(MODEL_FOLDER):
        if file.endswith(".pkl"):
            model_name = file.replace(".pkl", "")
            models[model_name] = joblib.load(f"{MODEL_FOLDER}/{file}")
            print(f"Loaded model: {model_name}")

@app.get("/")
def home():
    return {"message": "ML Deployment API Running"}

@app.post("/predict/{model_name}")
def predict(model_name: str, data: list):
    if model_name not in models:
        return {"error": "Model not found"}

    prediction = models[model_name].predict([data])
    return {"prediction": int(prediction[0])}