# Fake_News_Detection
An NLP model which predicts whether a news article is real or fake, along with a web app implemented using Flask




# Fake/Real News Classification Web App

A simple machine learning web app for text classification, built with Flask, trained using scikit-learn on Kaggle.
This project demonstrates end-to-end ML workflow: data preprocessing, model training, saving with `pickle`, and deploying an interactive web app.



## Features

* Preprocesses text using **NLTK** (stopword removal, lemmatization, etc.)
* ML models trained on Kaggle (`scikit-learn`, `pandas`, `numpy`)
* Interactive **web app** using Flask/Streamlit
* Simple, lightweight UI to input text and see predictions

---

## Project Structure

```
├── app.py             
├── vectorizer.pkl           
├── requirements.txt    
├── README.md           
├── text_cleaner.pkl
├── LICENSE
├── kaggle_fakenews_nb.ipynb
├── templates
   ├── index.html
```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YashJha12421/Fake_News_Detection.git
   cd text-classification-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   

   ```bash
   python app.py
   ```

---

## Model Training

* Dataset and training were handled in **Kaggle Notebooks**.

* Preprocessing steps include:

  * Lowercasing
  * Stopword removal
  * Lemmatization

* Models used: `Random Forest`, `Logistic Regression`, `XGBoost`

* Final model exported as `fake_news_model.pkl`, which used XGBoost with 99.76% accuracy, and loaded in the web app.

---

## Demo

<img width="1023" height="714" alt="image" src="https://github.com/user-attachments/assets/87d5a1ad-6ab3-47ba-b98e-9ae19cf215c1" />




---

## Visualizations & Results


* Logistic regression Accuracy: 0.9870


                          precision    recall  f1-score   support

                   0          0.99      0.98      0.99      4710
                   1          0.98      0.99      0.99      4270

            
          macro avg           0.99      0.99      0.99      8980
          weighted avg        0.99      0.99      0.99      8980


* Random Forest Accuracy: 0.9962

                      precision    recall  f1-score   support

                   0       1.00      1.00      1.00      4710
                   1       1.00      1.00      1.00      4270

   
           macro avg       1.00      1.00      1.00      8980
        weighted avg       1.00      1.00      1.00      8980
  
* XGBoost Accuracy: 0.9976

                      precision    recall  f1-score   support

                   0       1.00      1.00      1.00      4710
                   1       1.00      1.00      1.00      4270

     
           macro avg       1.00      1.00      1.00      8980
        weighted avg       1.00      1.00      1.00      8980



---





## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## Tech Stack

* **Python**
* **NLTK**
* **scikit-learn**
* **Flask/Streamlit**
* **Pandas, NumPy**

---

## License

MIT License

---


