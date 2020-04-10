from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'base.html')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('welcome')
            return HttpResponse('welcome')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/signup.html',{'form':form})
@login_required
def welcome(request):
    return render(request,'welcome.html')