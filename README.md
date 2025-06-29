# Stock-price-prediction
📈 Stock Price Prediction – AAPL (Apple Inc.)
A machine learning-based project that predicts the future closing price of Apple Inc. (AAPL) stock using historical data. It includes feature engineering and two predictive models: Linear Regression and Random Forest Regressor.
🧠 Features & Techniques
📊 Download real-time stock data using yFinance
🧹 Data cleaning and preprocessing
📈 Feature engineering with moving averages (50-day, 200-day)

🧪 Model training and evaluation using:
Linear Regression
Random Forest Regressor
📉 Metrics: R² Score and RMSE
🔮 Predict the next-day stock closing price based on latest data

💻 Technologies Used
Python 3.
yfinance
pandas, numpy
scikit-learn (sklearn)

## 📂 Project Structure
stock-price-app/
├── backend/
│ ├── app.py # Flask web server
│ ├── model.pkl # Trained machine learning model
│ ├── scaler.pkl # Scaler used during model training
│ ├── train_model.py # Script to train and save model
│ ├── requirements.txt # Python dependencies
│ ├── templates/
│ │ └── index.html # Frontend HTML form
│ └── static/
│ └── style.css # CSS styling

## 🚀 Features

- Accepts input: Open, High, Low, Volume, MA50, MA200
- Predicts the **Close Price** of a stock
- User-friendly HTML UI
- Machine learning model with preprocessing (scaler)
  
# HOW TO RUN THIS
->Install Required Packages
pip install -r requirements.txt
->Train the model
python train_model.py-
->Run Flask app
python app.py
