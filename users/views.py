from django.shortcuts import render , redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
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
    if request.method=='POST':

        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'profile  has been updated !')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request,'users/profile.html',context)