# EV-battery-life-predictor
An end-to-end Edge AI Machine Learning pipeline for Predictive Maintenance of Electric Vehicle (EV) Lithium-Ion Batteries. Uses a Deep Learning (ANN) model trained on the NASA Battery Dataset to predict Remaining Useful Capacity (Ah) based on real-time sensor telemetry. Built with TensorFlow, FastAPI, and vanilla JavaScript.


# 🔋 EV Battery Predictive Maintenance AI

This project is an end-to-end Machine Learning pipeline designed to predict the Remaining Useful Life (RUL) and State of Health (SoH) of Lithium-Ion batteries. By analyzing real-time resistance and temperature telemetry, the deep learning model predicts the remaining capacity (Amp-hours) of a battery, acting as an intelligent software fuse for Electric Vehicle (EV) motor controllers.

## 🚀 Live Demo
**[Insert your Render URL here once deployed, e.g., https://ev-battery-ai.onrender.com]**

## 🧠 Project Overview
Lithium-ion batteries degrade over time due to thermal wear and chemical degradation. This project uses the **NASA Prognostics Center Battery Dataset** to train an Artificial Neural Network (ANN) that maps internal battery resistance (`Re` and `Rct`) to its physical degradation curve. 

The project bridges the gap between Data Science and Edge Engineering by wrapping the Keras Deep Learning model in a lightning-fast **FastAPI** backend and serving an interactive web dashboard for real-time predictions.

## 🛠️ Tech Stack
* **Machine Learning:** Python, TensorFlow / Keras, Scikit-Learn, Pandas, NumPy
* **Backend API:** FastAPI, Uvicorn, Pydantic
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Deployment:** Render (Cloud Web Service)

## 📂 Project Structure
```text
ev-battery-predictor/
│
├── static/
│   └── index.html               # The interactive frontend dashboard
│
├── battery_life_model.h5        # Trained Keras Neural Network (ANN)
├── scaler.pkl                   # MinMax Scaler for feature normalization
├── label_encoder.pkl            # Encoder for categorical telemetry variables
├── main.py                      # FastAPI server and inference logic
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
