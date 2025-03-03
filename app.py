
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('fraud_model.pkl')
print("Model loaded successfully")

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    
    # Convert to DataFrame (expects same features as training data)
    input_data = pd.DataFrame([data])
    
    # Make prediction
    prediction = model.predict(input_data)
    result = 'Fraud' if prediction[0] == 1 else 'Legit'
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)