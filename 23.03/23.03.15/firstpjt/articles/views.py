from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def profile(request):
    info = {
        "name" : "lee" ,
        "age" : 25 ,
    }

    return render(request, "articles/profile.html", {'info': info})

def fruits(request):
    f_list = ["apple", "banana", "melon"]
    context = {
        'food' : f_list,
        'info' : info
    }
    return render(request, 'fruits.html', context)

def templates(request):
    return render(request, 'templates/base.html')