from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        text = request.POST['message']
        readtext(text)
    return  render(request, 'test_prosto/index.html')

   # return  render(request, 'test_prosto/results.html' ,context)

def readtext(str):
    global text
    def get(str):
        text = str
        print('def get(str)')
        return text
    text = get(str)