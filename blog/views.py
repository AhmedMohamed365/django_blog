from django.shortcuts import render
from django.http import HttpResponse

#imported models
from .models import Post
# Create your views here.



def Home(request):
    context = {
        'posts': Post.objects.all(),
        'title' : 'Home'
    }
    return render(request,'blog/home.html',context=context)
def about(request):
    return render(request,'blog/about.html')