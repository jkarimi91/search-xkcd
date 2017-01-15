from django.conf import settings
from django.core.management.base import BaseCommand
import os
import re
import requests
from sklearn.externals import joblib

class Command(BaseCommand):
    help = 'fetches xkcd comics'

    def handle(self, *args, **options):
        if not os.path.exists(settings.DATA_DIR):
            os.makedirs(settings.DATA_DIR)

        comics_file = os.path.join(settings.DATA_DIR, 'comics.p')
        if not os.path.exists(comics_file):
            comics = fetch_comics(1)
        else:
            comics = joblib.load(comics_file)
            comic_num = get_next_comic_num(comics[-1]['num'])
            comics.extend(fetch_comics(comic_num))

        joblib.dump(comics, comics_file)
        self.stdout.write(self.style.SUCCESS('Successfully fetched comics'))

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
    url = os.path.join(homepage, str(comic_num))
    r = requests.get(url)
    return r.content

def fetch_comics(comic_num):
    if comic_num is not None:
        comic_num = str(comic_num)
    comics = []
    while comic_num is not None:
        comic_json = get_comic_json(comic_num)
        comics.append(comic_json)
        comic_num = get_next_comic_num(comic_num)
    return comics

