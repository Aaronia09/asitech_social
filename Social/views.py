# Social/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login, authenticate 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment, Notification, Like
from django.contrib import messages


@login_required
def home(request):
       posts = Post.objects.all()
       return render(request, 'Social/home.html', {'posts': posts}) 
     
     
     
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Social/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'Social/login.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post.objects.create(user=request.user, content=content) 
        return redirect('post_detail', post_id=post.id)

    return render(request, 'Social/create_post.html')

def post_detail(request, post_id):
    post =get_object_or_404(Post,id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'Social/post_detail.html', {'post': post, 'comments': comments})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, "Vous avez retiré votre like de ce post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "Vous avez liké ce post.")
    
    return redirect('home')


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        
       
        Notification.objects.create(user=post.user, comment=comment) 
        
        return redirect('post_detail', post_id=post.id)  
    return render(request, 'Social/post_detail.html', {'post_id': post_id}) 

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'Social/notifications.html', {'notifications': user_notifications})
@login_required
def profile_view(request):
    return render(request, 'Social/profile.html')  

