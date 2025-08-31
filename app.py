

from flask import Flask, request, render_template
import pickle
import nltk
nltk.download("wordnet")
nltk.download("stopwords")

app = Flask(__name__)


with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z]", " ", text)
        words = text.split()
        words = [self.lemmatizer.lemmatize(w) for w in words if w not in self.stop_words]
        return " ".join(words)


with open("text_cleaner.pkl", "rb") as f:
    cleaner = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    article = request.form["article"]
    
    cleaned_article = cleaner.clean(article)
    
    article_vec = vectorizer.transform([cleaned_article])
    
    prediction = model.predict(article_vec)[0]
    result = "True" if prediction == 1 else "False"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
