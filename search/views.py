from django.shortcuts import render
from django.http import HttpResponse
from sklearn.externals import joblib
from sklearn.metrics.pairwise import linear_kernel
from django.conf import settings
import os.path

# Create your views here.
def search(request):
    query = request.GET.get('query')
    if query is None:
        return render(request, 'index.html')
    search_results = [r['img'] for r in get_search_results(query)]
    return render(request, 'list.html', {'search_results': search_results})

def get_search_results(query):
    model = joblib.load(os.path.join(settings.DATA_DIR, 'model.p'))
    tfidf = joblib.load(os.path.join(settings.DATA_DIR, 'tfidf.p'))
    comics = joblib.load(os.path.join(settings.DATA_DIR, 'comics.p'))

    query = model.transform([query])
    search_results = linear_kernel(query, tfidf).flatten()
    indices = search_results.argsort()[::-1]
    indices = filter(lambda i: search_results[i] > 0, indices)
    return [comics[i] for i in indices]
