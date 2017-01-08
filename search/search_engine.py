from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from string import punctuation
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from numpy import asarray, where

class SearchEngine(object):
    def __init__(self, comics):
        self.comics = asarray(comics)
        self.vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
        self.tfidf = self.vectorizer.fit_transform(c['text'] for c in comics)

    def search(self, query):
        query = self.vectorizer.transform([query])
        result = linear_kernel(query, self.tfidf).flatten()
        indices = result.argsort()[::-1]
        indices = filter(lambda i: result[i] > 0, indices)
        return self.comics[indices]

def tokenize(text):
    tokens = word_tokenize(text)
    return normalize(tokens)

def normalize(tokens):
    result = []
    stemmer = PorterStemmer()
    exclude = set(punctuation)
    for t in tokens:
        if t not in exclude:
            t = stemmer.stem(t.lower())
            result.append(t)
    return result
