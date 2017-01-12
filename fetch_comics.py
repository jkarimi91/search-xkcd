import os.path
import re
import requests
from sklearn.externals import joblib
from django.conf import settings

def get_comic_json(comic_num):
    homepage = 'http://xkcd.com'
    filename = 'info.0.json'
    url = os.path.join(homepage, comic_num, filename)
    r = requests.get(url)
    return r.json()

def get_next_comic_num(comic_num):
    comic_html = get_comic_html(comic_num)
    pattern = r'<a rel="next" href="/(\d+)/" accesskey="n">Next &gt;</a>'
    pattern = re.compile(pattern)
    matches = pattern.search(comic_html)
    return None if matches is None else matches.group(1)

def get_comic_html(comic_num):
    homepage = 'http://xkcd.com'
    url = os.path.join(homepage, comic_num)
    r = requests.get(url)
    return r.content

comics = []
comic_num = '1'

while comic_num is not None:
    comic_json = get_comic_json(comic_num)
    comics.append(comic_json)
    comic_num = get_next_comic_num(comic_num)

joblib.dump(comics, os.path.join(settings.DATA_DIR, 'comics.p'))
