from flask import Flask, request, jsonify, render_template
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from predict import predict_churn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    probability = predict_churn(data)
    return jsonify({'churn_probability': probability})

if __name__ == '__main__':
    app.run(debug=True)