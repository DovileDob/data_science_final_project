from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


#Spacy load because simple path does not work here
nlp = spacy.load("C:/Users/Dovilė/AppData/Local/Programs/Python/Python310/lib/site-packages/lt_core_news_md/lt_core_news_md-3.5.0")

#Text cleaning class, was not able to make it work from text_laundromat.py
class TextLaundromat:
    def open_stopwords(stopwords_path):
        with open(stopwords_path, "r", encoding="utf-8") as file:
            stopwords = [word.strip() for word in file.readlines()]

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

