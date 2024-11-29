from django.shortcuts import render , redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request:HttpRequest):
    if request.method =='POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           print('form is valid')
           username = form.cleaned_data.get('username')
           messages.success(request,f'account user {username} has registered!')
           return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render (request,'users/register.html',context={'form':form})

@login_required
def profile(request: HttpRequest):
    return render(request,'users/profile.html')