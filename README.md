# 🛡️ Phishing URL Detection System

A machine learning system that detects phishing URLs using a **CatBoost Classifier**, achieving **97.6% F1-score**, **98.6% Recall**, and **96.6% Precision**.

> Detect malicious URLs in real time using machine learning and URL-based security features.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![CatBoost](https://img.shields.io/badge/Model-CatBoost-orange)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.8% |
| F1-Score  | 97.6% |
| Recall    | 98.6% |
| Precision | 96.6% |

### Model

* Algorithm: CatBoost Classifier
* Experiment Tracking: MLflow + DagsHub
* Experiments Conducted: 10+

---

# 📖 Project Overview

This project identifies phishing websites by analyzing structural and security-related URL characteristics.

The system extracts more than 20 handcrafted features from a URL and uses a trained CatBoost model to classify it as:

* ✅ Legitimate
* 🚨 Phishing

The application supports:

* Single URL prediction
* Batch URL prediction via CSV upload
* REST API inference
* Docker deployment
* Experiment tracking with MLflow

---

# 🏗️ System Architecture

User URL
↓
Feature Extraction
↓
CatBoost Model
↓
Prediction + Confidence Score
↓
Flask API / Web Interface

---

# ✨ Features

* High-performance CatBoost model
* Flask web application
* REST API for real-time predictions
* Batch CSV prediction
* MongoDB integration
* MLflow experiment tracking
* Docker containerization
* Modular training and inference pipelines

---

# 📂 Project Structure

```text
NetworkSecurity/
│
├── networksecurity/
│   ├── components/          # Data ingestion, validation, training
│   ├── pipeline/            # Training & prediction pipelines
│   ├── cloud/               # MongoDB integration
│   ├── exception/           # Custom exceptions
│   ├── logging/             # Logging configuration
│   └── utils/               # Utility functions
│
├── notebooks/               # EDA and experimentation
├── templates/               # HTML templates
├── static/                  # CSS / JS assets
│
├── app.py                   # Flask application
├── main.py                  # Training pipeline entry point
├── Dockerfile               # Docker configuration
├── requirements.txt         # Project dependencies
├── setup.py                 # Package setup
└── README.md
```

---

# 🚀 Quick Start

## Option 1 — Docker

```bash
docker pull onkar1718/networksecurity-app:latest

docker run -p 5000:5000 onkar1718/networksecurity-app:latest
```

Open:

```text
http://localhost:5000
```

---

## Option 2 — Local Installation

```bash
git clone https://github.com/Korale05/NetworkSecurity.git

cd NetworkSecurity

pip install -r requirements.txt

python app.py
```

Open:

```text
http://localhost:5000
```

---

# 💻 Usage

## Web Interface

1. Launch the application
2. Enter a URL
3. Click Predict
4. View prediction and confidence score

---

## Batch Prediction

Upload a CSV file containing URLs and receive predictions for all entries.

---

## REST API

### Endpoint

```http
POST /predict
```

### Example Request

```python
import requests

response = requests.post(
    "http://localhost:5000/predict",
    json=data
)

print(response.json())
```

### Example Response

```json
{
  "prediction": "phishing",
  "confidence": 0.94,
  "risk_level": "high"
}
```

---

# 🤖 Model Training

Run the complete training pipeline:

```bash
python main.py
```

This performs:

1. Data ingestion
2. Data validation
3. Feature engineering
4. Model training
5. Model evaluation
6. MLflow logging

---

# 📊 Feature Engineering

The model analyzes 20+ URL-based features, including:

### Structural Features

* URL Length
* Number of Dots
* Number of Slashes
* Number of Hyphens
* Number of Special Characters

### Security Features

* HTTPS Presence
* IP Address Usage
* Suspicious Patterns

### Lexical Features

* Character Distribution
* URL Complexity Indicators

---

# 🛠️ Technology Stack

| Layer               | Technology             |
| ------------------- | ---------------------- |
| Machine Learning    | CatBoost, Scikit-learn |
| Backend             | Flask                  |
| Database            | MongoDB                |
| Experiment Tracking | MLflow, DagsHub        |
| Deployment          | Docker                 |
| Language            | Python                 |

---

# 🔗 Links

### GitHub Repository

https://github.com/Korale05/NetworkSecurity

### Docker Hub

https://hub.docker.com/r/onkar1718/networksecurity-app

### DagsHub

https://dagshub.com/Korale05/NetworkSecurity

---

# 📄 License

This project is licensed under the MIT License.

---

# 👤 Author

Onkar Korale

GitHub: https://github.com/Korale05

Machine Learning • MLOps • Security Analytics
