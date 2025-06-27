# 🧠 Future Interns ML Internship – Project Portfolio

Welcome to my Machine Learning Internship portfolio, completed under the **Future Interns ML Batch 03**. This repository showcases three end-to-end machine learning projects developed using real-world datasets, combining time series forecasting, deep learning, and NLP-based chatbot systems.

---

## 📁 Repository Structure

```
FUTURE-INTERNS-ML/
├── FUTURE_ML_01/
│   ├── Output.png
│   ├── SalesForecastingModel_by_AtishayJain.ipynb
│   ├── readme.md
│   ├── requirements.txt
│   └── sales_data_sample.csv
│
├── FUTURE_ML_02/
│   ├── StockPricePredictionModel_by_AtishayJain.ipynb
│   ├── output1.png
│   ├── output2.png
│   ├── readme.md
│   └── requirements.txt
│
├── FUTURE_ML_03/
│   ├── data/
│   ├── .env
│   ├── chatbot.py
│   ├── chatbot_ui.png
│   ├── connect_memory_with_llm.py
│   ├── create_memory_for_llm.py
│   ├── intent_generation.py
│   ├── readme.md
│   ├── requirements.txt
│   └── README.md


---

## 📊 Project 1: Sales Forecasting using Prophet

* Utilized Facebook Prophet to predict daily retail sales based on transactional history.
* Handled trend/seasonality tuning and changepoint optimization.
* **Final MAE**: \~16,855
* **Tools**: Python, Pandas, Prophet, Matplotlib

---

## 📈 Project 2: Stock Price Prediction with LSTM

* Designed an LSTM-based pipeline to predict future stock prices using windowed sequences.
* Preprocessed over 2000+ CSVs and implemented sequence-to-one regression.
* Evaluated predictions using RMSE and visual comparison.
* **Tools**: Python, Keras, NumPy, Matplotlib

---

## 💬 Project 3: Customer Support Chatbot with NLP

* Built an end-to-end FastAPI-based chatbot trained on real ticket data.
* Used Bi-LSTM for intent classification and LangChain + Groq for RAG semantic Q\&A.
* Integrated a modern HTML/CSS/JS frontend with avatars, chat history, and confidence scoring.
* **Tools**: TensorFlow, LangChain, Groq, ChromaDB, NLTK, FastAPI

---

## 🚀 Deployment

To run the chatbot locally:

```bash
cd src
uvicorn app:app --reload
```

Visit: `http://localhost:8000`

---

## 📚 Learnings

* Real-world time series forecasting & sequence modeling
* NLP-based intent classification and chatbot deployment
* Deep integration of front-end with ML APIs
* End-to-end ML system design with reproducibility and modularity

---

## 📬 Contact

If you'd like to collaborate or learn more about my work:
📧 [atishay.contact@gmail.com](mailto:atishay.contact@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/atishayjain)

---

> ✨ This internship gave me production-ready ML exposure and pushed me to integrate intelligence with interactivity.
