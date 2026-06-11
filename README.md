# 🛡️ Phishing URL Detection System

> End-to-end Machine Learning system for detecting phishing websites using CatBoost, MLflow, MongoDB, Flask, and Docker.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![CatBoost](https://img.shields.io/badge/CatBoost-ML-orange)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Deployment-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

## 🚀 Project Highlights

✅ Built an end-to-end phishing URL detection pipeline

✅ Trained and compared multiple ML experiments using MLflow

✅ Achieved **97.6% F1-Score** on unseen data

✅ Deployed as a Flask web application

✅ Supports REST API and batch predictions

✅ Containerized using Docker

✅ MongoDB integration for scalable storage

---

# 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.8% |
| F1 Score  | 97.6% |
| Recall    | 98.6% |
| Precision | 96.6% |

### Why Recall Matters

For phishing detection, missing a malicious URL is expensive.

The model achieves **98.6% recall**, meaning it successfully identifies nearly all phishing attempts while maintaining strong precision.

---

# 🎯 Problem Statement

Phishing websites are designed to imitate trusted services and steal sensitive information such as passwords, banking credentials, and personal data.

Traditional blacklist-based systems struggle to detect newly generated phishing domains.

This project uses machine learning to identify phishing URLs by analyzing their structure, lexical properties, and security indicators.

---

# 🏗️ System Architecture

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
Prediction Probability
    │
    ▼
Risk Assessment
    │
    ▼
Flask UI / REST API
```

---

# 📂 Project Structure

```text
NetworkSecurity/
│
├── networksecurity/
│   │
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

# ⚙️ Machine Learning Pipeline

The training workflow consists of:

1. Data Ingestion
2. Data Validation
3. Feature Engineering
4. Model Training
5. Hyperparameter Optimization
6. Model Evaluation
7. Experiment Tracking (MLflow)
8. Artifact Storage

---

# 📊 Feature Engineering

The model extracts more than 20 handcrafted URL features.

### Structural Features

* URL Length
* Number of Dots
* Number of Slashes
* Number of Hyphens
* Number of Special Characters

### Security Features

* HTTPS Usage
* Presence of IP Address
* Suspicious Domain Patterns

### Lexical Features

* Character Distribution
* URL Complexity Metrics
* Token-Based Signals

---

# 🛠️ Technology Stack

| Category            | Technology             |
| ------------------- | ---------------------- |
| Machine Learning    | CatBoost, Scikit-Learn |
| Experiment Tracking | MLflow, DagsHub        |
| Backend             | Flask                  |
| Database            | MongoDB                |
| Deployment          | Docker                 |
| Language            | Python                 |

---

# 🚀 Getting Started

## Run with Docker

```bash
docker pull onkar1718/networksecurity-app:latest

docker run -p 5000:5000 onkar1718/networksecurity-app:latest
```

Open:

```text
http://localhost:5000
```

---

## Run Locally

```bash
git clone https://github.com/Korale05/NetworkSecurity.git

cd NetworkSecurity

pip install -r requirements.txt

python app.py
```

---

# 🔌 REST API

### Endpoint

```http
POST /predict
```

### Sample Response

```json
{
  "prediction": "phishing",
  "confidence": 0.94,
  "risk_level": "high"
}
```

---

# 📈 Future Improvements

* Browser Extension
* SHAP Explainability Dashboard
* Real-Time Threat Intelligence Integration
* Kubernetes Deployment
* Online Learning Pipeline

---

# 🔗 Project Links

### GitHub Repository

https://github.com/Korale05/NetworkSecurity

### Docker Hub

https://hub.docker.com/r/onkar1718/networksecurity-app

### DagsHub

https://dagshub.com/Korale05/NetworkSecurity

---

# 👨‍💻 Author

### Onkar Korale

Machine Learning • MLOps • Cybersecurity

GitHub: https://github.com/Korale05

---

# 📄 License

This project is licensed under the MIT License.
