from comic import Comic
import string
import pickle

def get_raw_data():
    data = []
    c = Comic()
    data.append(c.json)
    while c.next_comic_number is not None:
        print c.comic_number
        c = Comic(c.next_comic_number)
        data.append(c.json)
    return data

def load_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def restructure(raw_data):
    result = []
    for d in raw_data:
        tmp = {}

        text = [d['transcript']]
        if d['alt'] not in d['transcript']:
            text.append(d['alt'])
        if d['title'] not in d['transcript']:
            text.append(d['title'])

        tmp['text'] = ' '.join(text)
        tmp['num'] = d['num']
        tmp['img'] = d['img']
        result.append(tmp)
    return result

