🛡️ Phishing URL Detection System
A machine learning system that detects phishing URLs with 97.6% accuracy using CatBoost algorithm.
📖 What is This?
Enter any URL and get instant prediction whether it's a phishing (malicious) site or legitimate. The system analyzes URL patterns and security features to identify suspicious websites.
✨ Features

High Accuracy Model: 97.6% F1-score, 98.6% recall, 96.6% precision
Web Interface: Easy-to-use Flask application
REST API: Real-time predictions
Batch Processing: Check multiple URLs at once
MLflow Tracking: 10+ experiments for model optimization
MongoDB Backend: Scalable data storage
Docker Ready: Containerized deployment

🚀 Quick Start
Using Docker
bashdocker pull onkar1718/networksecurity-app:latest
docker run -p 5000:5000 onkar1718/networksecurity-app:latest

# Visit http://localhost:5000
Local Setup
bashgit clone https://github.com/Korale05/NetworkSecurity.git
cd NetworkSecurity
pip install -r requirements.txt
python app.py

# Visit http://localhost:5000
💻 Usage
Web Interface

Open http://localhost:5000 in your browser
Enter a URL or upload CSV file with multiple URLs
Click "Check" to get predictions
View results with confidence scores

API Example
import requests


data = {
    "url": "https://suspicious-site.com/login",
    "url_length": 45,
    "num_dots": 3,
    "num_hyphens": 1,
    "num_underscores": 0,
    "num_slash": 2,
    "num_questionmark": 0,
    "num_equal": 0,
    "num_at": 0,
    "num_and": 0,
    "num_exclamation": 0,
    "num_space": 0,
    "num_tilde": 0,
    "num_comma": 0,
    "num_plus": 0,
    "num_asterisk": 0,
    "num_hashtag": 0,
    "num_dollar": 0,
    "num_percent": 0,
    "has_ip": 0,
    "has_https": 1
}

response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())

# Output: {"prediction": "phishing", "confidence": 0.94, "risk_level": "high"}

📊 Model Performance
Algorithm: CatBoost Classifier

F1-Score: 97.6%
Recall: 98.6% (catches most phishing URLs)
Precision: 96.6% (very few false alarms)
Accuracy: 97.8%

🏗️ Project Structure
NetworkSecurity/
├── networksecurity/
│   ├── components/         # ML pipeline components
│   ├── pipeline/           # Training & prediction pipelines
│   ├── cloud/              # MongoDB integration
│   └── logging/            # Logging system
├── templates/              # Flask web interface
├── notebooks/              # Data analysis
├── app.py                  # Flask application
├── main.py                 # Model training
├── Dockerfile              # Container configuration
└── requirements.txt

🤖 Training
Run the training pipeline:
bashpython main.py
This will train the model and save it with MLflow experiment tracking.

📊 URL Features Analyzed
The model examines 20+ security features:

URL length and structure
Number of special characters (dots, hyphens, slashes)
Security indicators (HTTPS, IP address usage)
Suspicious patterns

🛠️ Tech Stack

ML: CatBoost, scikit-learn
Tracking: MLflow, DagsHub
Backend: Flask, MongoDB
Deployment: Docker

🔗 Links

GitHub: https://github.com/Korale05/NetworkSecurity
DockerHub: https://hub.docker.com/r/onkar1718/networksecurity-app
DagsHub: https://dagshub.com/Korale05/NetworkSecurity

📄 License
MIT License