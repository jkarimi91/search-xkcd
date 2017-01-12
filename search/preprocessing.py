from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from string import punctuation

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
