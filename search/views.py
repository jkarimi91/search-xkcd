from django.shortcuts import render
from django.http import HttpResponse
from preprocessing import load_data
from search_engine import SearchEngine
#from sklearn.externals import joblib
from nltk.stem.porter import PorterStemmer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_results(request):
    data = load_data('search/data.p')
    #print nltk.__version__
    #s = PorterStemmer()
    #s.stem('oed')
    s = SearchEngine(data)
    query = request.GET['query']
    results = [r['img'] for r in s.search(query)]
    return render(request, 'list.html', {'results': results})
