# 📧 Email Spam Classifier

A production-ready Email Spam Classifier built using Machine Learning and NLP techniques.

## 📁 Project Structure
email-spam-classifier/
│
├── data/
│   ├── raw/
│   │   └── emails_dataset.csv
│   │
│   └── processed/
│       └── preprocessed_data.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   ├── data_preparation.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   └── text_transformation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   └── test_text_transformation.py
│
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Workflow
1. Data preprocessing & cleaning
2. Text transformation using NLP
3. Feature extraction using TF-IDF
4. Model training & evaluation
5. Model persistence using Pickle
6. Prediction using modular app

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- PyTest

## 📊 Model Output
- Spam / Not Spam classification

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/app.py
