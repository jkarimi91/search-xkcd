from django.conf import settings
from django.core.management.base import BaseCommand
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation

class Command(BaseCommand):
    help = 'fit the search engine model'

    def handle(self, *args, **options):
        comics = joblib.load(os.path.join(settings.DATA_DIR, 'comics.p'))
        model = TfidfVectorizer(tokenizer=tokenize, stop_words='english',
                                ngram_range=(1, 2))
        text_data = [extract_comic_text(c) for c in comics]
        tfidf = model.fit_transform(text_data)

        joblib.dump(model, os.path.join(settings.DATA_DIR, 'model.p'))
        joblib.dump(tfidf, os.path.join(settings.DATA_DIR, 'tfidf.p'))
        self.stdout.write(self.style.SUCCESS('Successfully fitted model'))

def extract_comic_text(comic):
    text = [comic['transcript']]
    if comic['alt'] not in comic['transcript']:
        text.append(comic['alt'])
    if comic['title'] not in comic['transcript']:
        text.append(comic['title'])
    return ' '.join(text)

def tokenize(text):
    tokens = word_tokenize(text)
    return normalize(tokens)

def normalize(tokens):
    normalized_tokens = []
    stemmer = PorterStemmer()
    exclude = set(punctuation)
    for t in tokens:
        if t not in exclude:
            t = stemmer.stem(t.lower())
            normalized_tokens.append(t)
    return normalized_tokens

