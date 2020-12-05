from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sitio(request):
    return render(request,"social/index.html")

def contacto(request):
    if request.method == "POST":
        subject = request.POST["asunto"]
        message = "La persona de nombre: " + request.POST["nombre"] + "\nCon el email: " + request.POST["email"] +"\nNos dice: " + request.POST["mensaje"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["ricardo.parrague@sansano.usm.cl", "pablo.camposa@sansano.usm.cl","juan.ariasr@sansano.usm.cl"]
        send_mail(subject,message,email_from,recipient_list)

        return render(request, "redirect.html")

    return render(request, "contacto.html")

def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado pa')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'social/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form' : form})

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user': user, 'posts': posts})

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')