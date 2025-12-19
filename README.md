# 📧 Email Spam Classifier

A production-ready **Email Spam Classifier** built using **Machine Learning and Natural Language Processing (NLP)**.  
This project classifies emails as **Spam** or **Not Spam (Ham)** using a clean, modular, and testable codebase.

---

## 🚀 Project Overview

Email spam detection is a classic NLP problem.  
In this project, raw email text is cleaned, transformed into numerical features, and classified using a trained Machine Learning model.

The project follows an **industry-level structure** with proper separation of:
- data
- notebooks
- source code
- models
- tests

---

## 📁 Project Structure

```text
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
