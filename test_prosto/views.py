from django.shortcuts import render ,redirect
import os

import scrap
import parsing_json 
import PLT_use_ex


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
        scrap.start(str)
        parsing_json.main(str)
        PLT_use_ex.image_compose()
        text = str
        print(os.getcwd())
        
        return text
    text = get(str)
    
def results(request):
    text_ = text
    context = {
        'text_':text_,
    }
    return render(request, 'test_prosto/results.html',context )