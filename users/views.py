from django.shortcuts import render , redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request:HttpRequest):
    if request.method =='POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           print('form is valid')
           username = form.cleaned_data.get('username')
           messages.success(request,f'account user {username} has registered!')
           return redirect('blog-home')
    else:
        form = UserCreationForm()

    return render (request,'users/register.html',context={'form':form})
