from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import User, UserProfile, UserPost
from .forms import editForm, editFormTwo, editFormPost
# Create your views here.

@login_required
def home(request):
    current_user = request.user.id 
    user = User.objects.get(id=current_user)
    userprofile = UserProfile.objects.get(user=current_user)
    form = editForm(instance=user)
    formTwo = editFormTwo(instance=userprofile)
    if request.method == 'POST':
        form = editForm(request.POST, instance=user)
        formTwo = editFormTwo(request.POST, instance=userprofile)
        if form.is_valid() and formTwo.is_valid:
            form.save()
            formTwo.save()
            return redirect('home:home')
    return render(request, "registration/home.html", {
        "form": form,
        "formtwo": formTwo
    }) 

def post(request):
    current_user = request.user
    if request.method == 'POST':
        detail = request.POST['add_post']
        UserPost.objects.create(user_id=request.user.id, post=detail)
        return redirect("home:post")
    
    return render(request, "registration/post.html", {
        "post": UserPost.objects.filter(user_id=current_user)
    }) 

def posts(request, id):
    posts = UserPost.objects.get(pk=id, user_id=request.user)
    if request.method == 'POST':
        posts.delete()
        return redirect('home:post')
    return render(request, "registration/posts.html", {
        "post": posts
    })
 
def editPost(request, id):
    post = UserPost.objects.get(id=id)
    form = editFormPost(instance=post)
    if request.method == 'POST':
        form = editFormPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home:post')
    return render(request, 'registration/edit.html', {
        'form': form
    })

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form })
