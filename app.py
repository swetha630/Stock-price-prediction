
print("App.py is starting...")
from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load(os.path.join("model.pkl"))
scaler = joblib.load(os.path.join("scaler.pkl"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        open_price = float(request.form['open'])
        high = float(request.form['high'])
        low = float(request.form['low'])
        volume = float(request.form['volume'])
        ma50 = float(request.form['ma50'])
        ma200 = float(request.form['ma200'])

        features = np.array([[open_price, high, low, volume, ma50, ma200]])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        return render_template('index.html', prediction=f"Predicted Close Price: ${prediction:.2f}")

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    print("App.py is starting...")
    print("Flask server starting at http://127.0.0.1:5000")
    app.run(debug=True)
