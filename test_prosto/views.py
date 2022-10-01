from django.shortcuts import render ,redirect

import requests as R
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

# Create your views here.
def index(request):
    if request.method=="POST":
        text = request.POST['message']
        readtext(text)
        return  redirect(results)
    return render(request, 'test_prosto/index.html')


   # return  render(request, 'test_prosto/results.html' ,context)

def readtext(str):
    global text
    def get(str):
        text = str
        print('def get(str)')
        return text
    text = get(str)
    
def results(request):
    text_ = text
    context = {
        'text_':text_
    }
    return render(request, 'test_prosto/results.html',context )