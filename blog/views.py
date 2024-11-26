from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [

    {'author': 'Ahmed',
     'title': 'how to use LLM in production',
     'content': 'First post I created by hand',
     'date_posted':'August 27 , 2018'
     },

     {'author': 'Hassan',
     'title': 'how to play Uncharted 4',
     'content': 'First post I created by hand',
     'date_posted':'August 28 , 2018'
     }
]

def Home(request):
    context = {
        'posts': posts,
        'title' : 'home'
    }
    return render(request,'blog/home.html',context=context)
def about(request):
    return render(request,'blog/about.html')