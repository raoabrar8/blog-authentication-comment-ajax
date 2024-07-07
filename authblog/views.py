from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, BlogForm, CommentForm
# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Comment, Blog
from django.http import JsonResponse

def blogHome(request):
    blogs = Blog.objects.all()
    return render(request, 'authblog/blogHome.html', {'blogs':blogs})

# Blog APp views
@login_required
def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = blog.comments.all()
    form = None  # Initialize form as None by default

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Comment added successfully!'}, status=200)
            else:
                return redirect('blog_details', id=blog.id)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = CommentForm()  

    return render(request, 'authblog/blog_details.html', {'blog': blog, 'comments': comments, 'form': form})

# @login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.auhtor = request.user
            blog.save()
            return redirect('blogHome')
        
    else:
        form = BlogForm()
    return render(request, 'authblog/create_blog.html', {'form':form})

@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:
        return redirect('blog_details', id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_details', id=blog.id)
    else:
        form = BlogForm()
    return render(request, 'authblog/update_blog.html', {'form':form, 'blog':blog})


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:
        return redirect('blog_details', id=id)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('blogHome')
    return render(request, 'authblog/delete_blog.html', {'blog':blog})









# comment view




# authentications views
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
                return redirect('blogHome')
            else:
                message = 'Credential Invalid!'
        except User.DoesNotExist:
            message = 'User Does Not Exist'
            
    context = {'message': message}
    return render(request, 'authblog/login.html', context)
            
            
            
def Logout(request):
    logout(request)
    return redirect('blogHome')
    
