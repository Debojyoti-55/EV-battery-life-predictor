# 🔋 EV Battery Predictive Maintenance AI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

This project is an end-to-end Machine Learning pipeline designed to predict the Remaining Useful Life (RUL) and State of Health (SoH) of Lithium-Ion batteries. By analyzing real-time internal resistance and temperature telemetry, the deep learning model predicts the remaining capacity (Amp-hours) of a battery, acting as an intelligent software fuse for Electric Vehicle (EV) motor controllers.

## 🚀 Live Demo
**[Insert your Render URL here, e.g., https://ev-battery-ai.onrender.com]**

## 🧠 Project Overview
Lithium-ion batteries degrade over time due to thermal wear and chemical degradation. This project uses the **NASA Prognostics Center Battery Dataset** to train an Artificial Neural Network (ANN) that maps internal battery resistance (`Re` and `Rct`) to its physical degradation curve. 

The project bridges the gap between Data Science and Edge Engineering by wrapping the Keras Deep Learning model in a lightning-fast **FastAPI** backend and serving an interactive HTML/JS web dashboard for real-time predictions.

## 🛠️ Tech Stack
* **Machine Learning:** Python, TensorFlow / Keras, Scikit-Learn, Pandas, NumPy
* **Backend API:** FastAPI, Uvicorn, Pydantic
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Deployment:** Render (Cloud Web Service)

## 📂 Repository Structure

ev-battery-predictor/
│
├── static/
│   └── index.html               # The interactive frontend web dashboard
│
├── battery_life_model.h5        # Trained Keras Neural Network (ANN)
├── scaler.pkl                   # MinMax Scaler for feature normalization
├── label_encoder.pkl            # Encoder for categorical telemetry variables
├── main.py                      # FastAPI server and ML inference logic
├── requirements.txt             # Python dependencies for deployment
└── README.md                    # Project documentation


## 📊 The Data & Model Architecture
* **Dataset:** NASA Battery Dataset (Test batteries: B0005, B0006, B0007, B0018)
* **Features Used:** `ambient_temperature`, `Re` (Electrolyte Resistance), `Rct` (Charge Transfer Resistance).
* **Target:** `Capacity` (Amp-hours remaining).
* **Neural Network Architecture:** 
  * Input Layer
  * Dense (64 units, ReLU activation)
  * Dropout (20%)
  * Dense (32 units, ReLU activation)
  * Dropout (20%)
  * Dense (1 unit, Linear activation)
* **Training Details:** Optimized using the Adam optimizer and tracked via Mean Squared Error (MSE). Implemented **Early Stopping** to prevent overfitting and capture the mathematically optimal network weights.

## 💻 How to Run Locally

1. **Clone the repository:**
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME

2. **Create a virtual environment (Recommended):**
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate

3. **Install the dependencies:**
   pip install -r requirements.txt

4. **Start the FastAPI Server:**
   uvicorn main:app --reload

5. **Access the Web Interface:**
   Open your browser and navigate to `http://localhost:8000` to view the interactive dashboard.

## 🌐 API Documentation
If you want to integrate this model into a physical microcontroller (like an ESP32 or Raspberry Pi Pico) or a mobile app, you can make a `POST` request directly to the API endpoint.

**Endpoint:** `POST /predict`

**Request Payload (JSON):**
{
    "ambient_temperature": 24.0,
    "Re": 0.056,
    "Rct": 0.200
}

**Response (JSON):**
{
    "predicted_capacity_Ah": 1.5066
}

## ☁️ Deployment (Render)
This project is configured for seamless free deployment on **Render.com**. 
1. Push this code to a public GitHub repository.
2. Log into Render and click **New + -> Web Service**.
3. Connect your GitHub repository.
4. Set the **Build Command** to: `pip install -r requirements.txt`
5. Set the **Start Command** to: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click Deploy!

## 👨‍💻 Author
**Debojyoti Bhattacharjee**
* Built as part of a Predictive Maintenance and Embedded Edge AI study.