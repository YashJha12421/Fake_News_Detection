# Fake_News_Detection
An ML model which predicts whether a news article is real or fake, along with a web app implemented using Flask




# 📝 Fake/Real News Classification Web App

A simple machine learning web app for text classification, built with Flask/Streamlit, trained using scikit-learn on Kaggle.
This project demonstrates end-to-end ML workflow: data preprocessing, model training, saving with `pickle`, and deploying an interactive web app.



## 🚀 Features

* Preprocesses text using **NLTK** (stopword removal, lemmatization, etc.)
* ML models trained on Kaggle (`scikit-learn`, `pandas`, `numpy`)
* Interactive **web app** using Flask/Streamlit
* Simple, lightweight UI to input text and see predictions

---

## 📂 Project Structure

```
├── app.py              # Main Flask/Streamlit app
├── model.pkl           # Trained model (scikit-learn, pickled)
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/text-classification-app.git
   cd text-classification-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

   or (if Flask)

   ```bash
   python app.py
   ```

---

## 📊 Model Training

* Dataset and training were handled in **Kaggle Notebooks**.

* Preprocessing steps include:

  * Lowercasing
  * Stopword removal
  * Lemmatization

* Models used: `Naive Bayes`, `Logistic Regression`, etc.

* Final model exported as `model.pkl` and loaded in the web app.

---

## 🎥 Demo

👉 [Live Demo on Streamlit Cloud](https://your-streamlit-link) *(if deployed)*

*(Screenshot of the web app UI can go here)*

---

## 📖 Visualizations & Results

* Example performance metrics (Accuracy, F1-score, Confusion Matrix)
* Example feature importance (top words contributing to classification)

*(Add charts/screenshots here — from Kaggle notebook)*

---

## 📌 Future Improvements

* Add support for multiple ML models to compare
* Enhance UI with more interactivity
* Deploy with Docker/Heroku

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 🛠️ Tech Stack

* **Python**
* **NLTK**
* **scikit-learn**
* **Flask/Streamlit**
* **Pandas, NumPy**

---

## 📜 License

MIT License

---

Do you want me to also **include visuals (accuracy chart, confusion matrix, word cloud, etc.)** in the README itself, or keep them only in your **Kaggle notebook** and just reference them in the README?
