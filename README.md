# 📧 Email Spam Classifier

A production-ready Email Spam Classifier built using Machine Learning and NLP techniques.

## 📁 Project Structure
- data/
  - raw/: Original dataset
  - processed/: Cleaned and preprocessed data
- notebooks/: Jupyter notebooks for EDA & training
- src/: Modular application code
- models/: Trained ML model & vectorizer
- tests/: Unit tests
- requirements.txt: Dependencies

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
