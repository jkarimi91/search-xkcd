from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from search.preprocessing import tokenize, extract_comic_text
from django.conf import settings
import os.path

comics = joblib.load(os.path.join(settings.DATA_DIR, 'comics.p'))
model = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
text_data = [extract_comic_text(c) for c in comics]
tfidf = model.fit_transform(text_data)

joblib.dump(model, os.path.join(settings.DATA_DIR, 'model.p'))
joblib.dump(tfidf, os.path.join(settings.DATA_DIR, 'tfidf.p'))
