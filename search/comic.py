import requests
import re
import os.path

class Comic(object):
    _homepage_url = 'http://xkcd.com'
    _json_filename = 'info.0.json'
    _pattern = r'<a rel="next" href="/(\d+)/" accesskey="n">Next &gt;</a>'
    _pattern = re.compile(_pattern)

    def __init__(self, comic_number=1):
        self.comic_number = str(comic_number)
        self.next_comic_number = self._get_next_comic_number()
        self.json = self._get_json()

    def _get_next_comic_number(self):
        html = self._get_html()
        matches = Comic._pattern.search(html)
        return None if matches is None else matches.group(1)

    def _get_html(self):
        url = os.path.join(Comic._homepage_url, self.comic_number)
        r = requests.get(url)
        return r.content

    def _get_json(self):
        url = os.path.join(Comic._homepage_url, self.comic_number)
        url = os.path.join(url, Comic._json_filename)
        r = requests.get(url)
        return r.json()
