from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import pickle
import numpy as np
import uvicorn
import os

app = FastAPI()

# 1. Load the AI Brain and Tools
model = load_model("battery_life_model.h5")
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

class SensorData(BaseModel):
    ambient_temperature: float
    Re: float
    Rct: float

# 2. The API Endpoint (Backend)
@app.post("/predict")
def predict_capacity(data: SensorData):
    type_encoded = label_encoder.transform(['discharge'])[0]
    input_features = np.array([[type_encoded, data.ambient_temperature, data.Re, data.Rct]])
    input_scaled = scaler.transform(input_features)
    prediction = model.predict(input_scaled)
    return {"predicted_capacity_Ah": float(prediction[0][0])}

# 3. Mount the Frontend (Serve HTML/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join("static", "index.html"))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)