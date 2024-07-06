from django.shortcuts import render, redirect
from .forms import SignUpForm
# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'authblog/blogHome.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('login')
                 
            except IntegrityError:
                form.add_error('username', 'Username already Exist!')
    else:
        form = SignUpForm()     
    return render(request, 'authblog/signup.html', {'form':form})


def UserLogin(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        print(username)
        print(password)
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Credential Invalid!'
        except User.DoesNotExist:
            message = 'User Does Not Exist'
            
    context = {'message': message}
    return render(request, 'authblog/login.html', context)
            
            
            
def Logout(request):
    logout(request)
    return redirect('home')

@login_required
def index(request):
    return render(request, 'authblog/index.html')
    
