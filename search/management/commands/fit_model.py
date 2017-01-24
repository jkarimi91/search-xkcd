from django.conf import settings
from django.core.management.base import BaseCommand
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation

class Command(BaseCommand):
    help = 'fit the search engine model'

    def handle(self, *args, **options):
        comics = joblib.load(os.path.join(settings.DATA_DIR, 'comics.p'))
        text = [extract_text(c) for c in comics]
        model = TfidfVectorizer(tokenizer=tokenize, ngram_range=(1, 2))
        tfidf = model.fit_transform(text)

        joblib.dump(model, os.path.join(settings.DATA_DIR, 'model.p'))
        joblib.dump(tfidf, os.path.join(settings.DATA_DIR, 'tfidf.p'))
        self.stdout.write(self.style.SUCCESS('Successfully fitted model'))

def extract_text(comic):
    text = [comic['transcript']]
    if comic['alt'] not in comic['transcript']:
        text.append(comic['alt'])
    if comic['title'] not in comic['transcript']:
        text.append(comic['title'])
    return ' '.join(text)

def tokenize(text):
    tokens = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    stop_words = stopwords.words('english')
    exclude = set(punctuation).union(set(stop_words))
    return [stemmer.stem(t) for t in tokens if t not in exclude]

