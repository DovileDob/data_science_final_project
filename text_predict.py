import pickle
import tkinter as tk
import numpy as np
import spacy
from tkinter import messagebox
import text_laundromat
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved model
    # Spacy Random Forest Classificator model
pickled_model_spacy_rf = pickle.load(open('rf_model.pkl', 'rb'))
    # Tf-IDF Logical Regression model
pickled_model_tfidf_lr = pickle.load(open('lr_tfidf_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

#Spacy load because simple path does not work here
nlp = spacy.load("C:/Users/Dovilė/AppData/Local/Programs/Python/Python310/lib/site-packages/lt_core_news_md/lt_core_news_md-3.5.0")

#Text cleaning class, was not able to make it work from text_laundromat.py
class TextLaundromat:
    def __init__(self, stopwords_path):
        with open(stopwords_path, "r", encoding="utf-8") as file:
            self.stopwords = [word.strip() for word in file.readlines()]

    def clean_text(self, text):
        cleaned_text = self._remove_html_tags(text)
        cleaned_text = self._normalize_text(cleaned_text)
        cleaned_text = self._remove_stopwords(cleaned_text)
        # Spacy vectorize
        # cleaned_text = self._vectorize_text(cleaned_text)
        # cleaned_text = np.array(cleaned_text)
        # Spacy lemitize
        cleaned_text = self._lemitize_text(cleaned_text)
        return cleaned_text

    def _remove_html_tags(self, text):
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'\b\w+\.(?:jpg|jpeg|png|gif)\b', '', text)
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    def _normalize_text(self, text):
        reviews = ""
        for x in text:
            if x.isalnum():
                reviews = reviews + x
            else:
                reviews = reviews + " "
        return reviews

    def _remove_stopwords(self, text):
        words = word_tokenize(text)
        return ' '.join([x for x in words if x not in self.stopwords])

    def _vectorize_text(self, text):
        doc = nlp(text)
        return doc.vector

    def _lemitize_text(self, text):
        doc = nlp(text)
        return ' '.join([token.lemma_ for token in doc])

# Create a function to clean the input text and get the predicted value

def get_prediction():
    laundromat = TextLaundromat("stops_lt.txt")
    text = input_text.get()
    text = text.lower()
    cleaned_text = laundromat.clean_text(text)  # Use the clean_text function from text_laundromat.py

    # Spacy vectorize and random forest classificator predict
    # prediction = pickled_model_spacy_rf.predict([cleaned_text])[0]
    # Tf-IDF vectorize and logical regression predict
    cleaned_text = tfidf.transform([cleaned_text])
    prediction = pickled_model_tfidf_lr.predict(cleaned_text)[0]
    messagebox.showinfo("Prediction", f"The predicted value is: {prediction}")


# Create a Tkinter window
window = tk.Tk()
window.title("Text Classification")

# Create a label and text input for the user input
input_label = tk.Label(window, text="Input text:")
input_label.pack()
input_text = tk.Entry(window, width=50)
input_text.pack()
predict_button = tk.Button(window, text="Predict", command=get_prediction)
predict_button.pack()
# get_prediction()

# Start the Tkinter event loop
window.mainloop()