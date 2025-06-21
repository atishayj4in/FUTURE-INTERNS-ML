## 📊 Stock Price Prediction

### 🚀 Objective
Predict future stock closing prices using past historical data and LSTM neural networks.

---

### 🧰 Tools Used
- Python
- yfinance
- Pandas, NumPy, Matplotlib
- scikit-learn
- TensorFlow (Keras LSTM)
- Google Colab

---

### 🔍 Key Steps
- Data collection using yfinance
- Preprocessing and scaling with MinMaxScaler
- Windowed time series dataset creation (lookback = 60 days)
- LSTM model training and tuning
- Evaluation using MAE, RMSE, R2
- Plotting predicted vs actual prices

---

### 📈 Results
- Final MAE: 3.67
- RMSE: 4.63
- R2 Score: 0.9681
- Model showed strong performance on multiple stocks including AAPL, A, B, and Z.

---

### 📎 Output Sample
Actual vs Predicted Plot (AAPL Stock)
![AAPL Output](output1.png)
Actual vs Predicted Plot (A Stock)
![A Output](output2.png)

---

### 📁 Dataset
- Yahoo Finance API (via yfinance)
- Stock symbols: AAPL, A, B, Z

---

### 💡 Learnings
- Built an end-to-end time series prediction model
- Learned to structure datasets for LSTM input
- Understood evaluation metrics and why MAE > MAPE for stocks
- Developed modular, scalable forecasting pipeline
