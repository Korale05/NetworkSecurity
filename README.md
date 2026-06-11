# 🛡️ Phishing URL Detection System

Machine learning system that classifies URLs as **Phishing** or **Legitimate** using a CatBoost classifier trained on 20+ structural, lexical, and security-related URL features.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/Model-CatBoost-orange" />
  <img src="https://img.shields.io/badge/Backend-Flask-green" />
  <img src="https://img.shields.io/badge/Database-MongoDB-brightgreen" />
  <img src="https://img.shields.io/badge/Deployment-Docker-blue" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

## 📑 Table of Contents

* Overview
* Results
* Demo
* Architecture
* Project Structure
* Getting Started
* Usage
* Training Pipeline
* Feature Engineering
* Tech Stack
* Future Improvements
* Links
* License

---

## 📖 Overview

Phishing attacks remain one of the most common cybersecurity threats. Traditional blacklist-based approaches fail to detect newly generated malicious URLs.

This project uses machine learning to identify phishing URLs based on their structure and security characteristics.

### Key Features

✅ Real-time URL prediction

✅ Batch CSV prediction

✅ REST API support

✅ MLflow experiment tracking

✅ MongoDB integration

✅ Docker deployment

✅ End-to-end training pipeline

---

## 📊 Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.8% |
| F1-Score  | 97.6% |
| Recall    | 98.6% |
| Precision | 96.6% |

### Best Model

* Algorithm: CatBoost Classifier
* Experiments Tracked: 10+
* Tracking Platform: MLflow + DagsHub

### Why Recall Matters

The system achieves **98.6% Recall**, meaning it successfully catches nearly all phishing URLs while maintaining high precision.

---

## 🖼️ Demo

### Web Interface

Add screenshots here:

```text
docs/homepage.png
docs/prediction.png
docs/batch_prediction.png
```

Example:

```markdown
![Home](docs/homepage.png)
```

---

## 🏗️ System Architecture

```text
User URL
    │
    ▼
Feature Extraction
(20+ Features)
    │
    ▼
CatBoost Classifier
    │
    ▼
Prediction
+ Confidence Score
    │
    ▼
Flask Web App / REST API
```

---

## 📂 Project Structure

```text
NetworkSecurity/
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── cloud/
│   │   └── mongo_db.py
│   │
│   ├── exception/
│   ├── logging/
│   └── utils/
│
├── notebooks/
├── templates/
├── static/
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🚀 Getting Started

### Docker Deployment

```bash
docker pull onkar1718/networksecurity-app:latest

docker run -p 5000:5000 onkar1718/networksecurity-app:latest
```

Visit:

```text
http://localhost:5000
```

---

### Local Installation

```bash
git clone https://github.com/Korale05/NetworkSecurity.git

cd NetworkSecurity

pip install -r requirements.txt

python app.py
```

---

## 💻 Usage

### Web Application

1. Open the application
2. Enter a URL
3. Click Predict
4. View prediction and confidence score

---

### Batch Prediction

Upload a CSV file containing URLs and receive predictions for all entries.

---

### REST API

Endpoint:

```http
POST /predict
```

Example:

```python
import requests

response = requests.post(
    "http://localhost:5000/predict",
    json=data
)

print(response.json())
```

Response:

```json
{
  "prediction": "phishing",
  "confidence": 0.94,
  "risk_level": "high"
}
```

---

## 🤖 Training Pipeline

Run:

```bash
python main.py
```

Pipeline Stages:

1. Data Ingestion
2. Data Validation
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. MLflow Logging
7. Artifact Saving

---

## 📊 Feature Engineering

The model extracts more than 20 URL-based features.

### Structural Features

* URL Length
* Number of Dots
* Number of Slashes
* Number of Hyphens
* Number of Special Characters

### Security Features

* HTTPS Usage
* Presence of IP Address
* Suspicious Patterns

### Lexical Features

* Character Distribution
* URL Complexity Indicators

---

## 🛠️ Technology Stack

| Category            | Technology             |
| ------------------- | ---------------------- |
| Machine Learning    | CatBoost, Scikit-learn |
| Backend             | Flask                  |
| Database            | MongoDB                |
| Experiment Tracking | MLflow, DagsHub        |
| Deployment          | Docker                 |
| Language            | Python                 |

---

## 🔮 Future Improvements

* Real-time browser extension
* SHAP explainability dashboard
* Kubernetes deployment
* Online learning pipeline
* Threat intelligence integration

---

## 🔗 Links

### Repository

https://github.com/Korale05/NetworkSecurity

### Docker Hub

https://hub.docker.com/r/onkar1718/networksecurity-app

### DagsHub

https://dagshub.com/Korale05/NetworkSecurity

---

## 📄 License

Distributed under the MIT License.

---

## 👨‍💻 Author

**Onkar Korale**

GitHub: https://github.com/Korale05

Machine Learning • MLOps • Cybersecurity
