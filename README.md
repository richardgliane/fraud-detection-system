# Financial Fraud Detection System

Welcome to my **Financial Fraud Detection System**—a practical machine learning project I developed to detect fraudulent transactions using the Kaggle Credit Card Fraud Detection dataset. This project showcases my skills in Python, machine learning, and the development of a RESTful API. It includes a trained Random Forest model and a Flask-based API for real-time predictions. Let’s dive into the details!

---

## Project Overview

- **Objective**: Build and deploy a model to identify fraudulent credit card transactions, addressing the challenge of imbalanced datasets.
- **Technologies**: Python, Pandas, scikit-learn, Flask, matplotlib.
- **Dataset**: [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) (download `creditcard.csv` manually).

---

## Features

- **Data Processing**: Handles a dataset of over 284,000 transactions with feature engineering.
- **Model Training**: Utilizes a Random Forest Classifier optimized for imbalanced data.
- **RESTful API**: Provides a `/predict` endpoint (POST) for real-time fraud predictions using JSON data.
- **Extensibility**: Designed for future enhancements like Dockerization or cloud deployment.

---

## Setup Instructions

### Prerequisites
- Python 3.8+ (e.g., 3.10 recommended).
- GitHub Desktop or Git.
- A Kaggle account for the dataset.

### Set Up a Virtual Environment
To isolate dependencies, create and activate a virtual environment:
- **Windows (cmd):**
```bash
python -m venv fraud_env
fraud_env\Scripts\activate
```
	
### Install Dependencies
``` bash
pip install -r requirements.txt
```
	
### Download the Dataset
Obtain creditcard.csv from Kaggle and place it in the project root.

### Train the Model
``` bash
python train_model.py
```

This generates fraud_model.pkl (takes a few minutes due to dataset size).

### Run the API
``` bash
python app.py
```

### Access the server
http://localhost:5000


## Testing the API
With the Flask app running, test the /predict endpoint:

### Using curl (recommended in Command Prompt):
```bash
curl -X POST -H "Content-Type: application/json" -d "@test.json" http://localhost:5000/predict
```

**Expected Output**: ```{"prediction": "Legit"}```

**Note**: Use Command Prompt (cmd) for reliability. PowerShell may misparse the command, causing errors (e.g., treating JSON as options).

### Using Python (reliable alternative):
```bash
python -c "import requests; data = open('test.json').read(); r = requests.post('http://localhost:5000/predict', headers={'Content-Type': 'application/json'}, data=data); print(r.text)"
```

**Expected Output**: ```{"prediction": "Legit"}```

**Additional Notes**:
The root URL (http://localhost:5000) returns 404 in a browser since it’s a POST-only API. Use /predict with POST requests.

A sample test.json is included. Ensure it matches the dataset’s feature structure.


## Project Structure

fraud-detection-system/
├── train_model.py    # Trains and saves the Random Forest model
├── app.py            # Flask API for predictions
├── requirements.txt  # Dependency list
├── README.md         # Project documentation
├── test.json         # Sample input for testing
├── .gitignore        # Excludes large files (e.g., fraud_model.pkl, creditcard.csv)
└── Fraud_API_Testing.ipynb  # Jupyter notebook for interactive testing

## Key Learnings

* Mastered handling imbalanced datasets with Random Forest.

* Gained experience in building and deploying a RESTful API with Flask.

* Overcame shell-specific challenges (e.g., PowerShell vs. cmd) to ensure robust testing.

## Future Enhancements

* Dockerization: Containerize the app for scalable deployment.

* Cloud Integration: Deploy to AWS or Heroku.

* Advanced Visualization: Add confusion matrices or feature importance plots in the notebook.

* Model Improvement: Experiment with neural networks (e.g., TensorFlow).

## Why This Matters

This project demonstrates my ability to tackle real-world AI challenges, particularly in financial fraud detection. It combines data preprocessing, machine learning, and RESTful API development, making it a strong portfolio piece. I’d love to discuss how I can bring this expertise to your team!


