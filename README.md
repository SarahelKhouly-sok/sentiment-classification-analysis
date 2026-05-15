# 😊 Sentiment Analysis & Emotion Classification Project

## 📌 Project Overview

This project is a Machine Learning-based Sentiment Analysis system designed to classify text into three emotions:

* 😡 Anger
* 😨 Fear
* 😊 Joy

The project uses Natural Language Processing (NLP) techniques along with multiple machine learning models to analyze and predict emotions from textual input.

---

## 🧠 Models Compared

Several machine learning algorithms were trained and evaluated to determine the best-performing model:

* XGBoost
* Random Forest
* Decision Tree
* Logistic Regression

After comparison, **XGBoost** achieved the highest overall performance and was selected as the final model.

---

## ⚙️ NLP Preprocessing

The project uses **spaCy** for text preprocessing and cleaning, including:

* Tokenization
* Lemmatization
* Stopword removal
* Punctuation removal

Feature extraction was performed using **TF-IDF Vectorization**.

---

## 📊 Final Model Performance (XGBoost)

| Emotion | Precision | Recall | F1-Score |
| ------- | --------- | ------ | -------- |
| Anger   | 0.91      | 0.95   | 0.93     |
| Fear    | 0.96      | 0.90   | 0.93     |
| Joy     | 0.95      | 0.96   | 0.96     |

### ✅ Overall Accuracy

* **Accuracy:** 94%
* **Macro Average F1-Score:** 0.94
* **Weighted Average F1-Score:** 0.94

---

## 🛠️ Technologies Used

* Python
* spaCy
* Scikit-learn
* XGBoost
* Pandas
* NumPy
* TF-IDF Vectorizer
* Flask 

---

## 📂 Project Structure

```bash
├── API/
├── Dataset/
├── Notebooks/
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <repository-link>
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

---

## 🎯 Project Goal

The goal of this project is to demonstrate how Natural Language Processing and Machine Learning can be used to automatically detect human emotions from text with high accuracy.

---

## 📈 Future Improvements

* Add more emotion categories
* Deploy the model on a cloud platform
* Improve preprocessing pipeline
* Integrate Deep Learning models such as LSTM or BERT

---

## 👩‍💻 Author

Sarah Osama El Khouly

