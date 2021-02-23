from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User(username = username)
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect('index')
        else:
            form = RegisterForm(request.POST)
            return render(request , 'register.html' , {'form' :form})
    else:
        form = RegisterForm(request.POST)
        return render(request , 'register.html' , {'form' :form})


def log_in(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username , password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            form = LoginForm(request.POST)
            return render(request , 'login.html' , {'form' :form})
    else:
        form = LoginForm(request.POST)
        return render(request , 'login.html' , {'form' :form})



def log_out(request):
    logout(request)
    return redirect('index')





