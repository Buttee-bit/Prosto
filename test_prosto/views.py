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
    global text, Path_image
    def get(str):
        scrap.start(str)
        parsing_json.main(str)
        PLT_use_ex.image_compose()
        text = str
        Path_image = r'{text}/1.jpg'
        print(os.getcwd())
        
        return text, Path_image
    text, Path_image = get(str)
    
def results(request):
    Path_image_ = Path_image
    text_ = text
    context = {
        'text_':text_,
        'Path_image_':Path_image_
    }
    return render(request, 'test_prosto/results.html',context )