from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def profile_detail(request,username):
    user = get_object_or_404(User,username=username)
    profile = user.profile
    articles = user.articles.all()
    return render(request, "users/profile_detail.html",{"profile":profile,"articles":articles})


@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("users:profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "users/profile_edit.html", {"form": form})


@login_required
def follow_user(request,username):
    user = get_object_or_404(User,username=username)
    profile= user.profile
    if request.user == profile.user:
        return redirect('users:profile',username=username)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)
    return redirect("users:profile",username=username)


@login_required
def following_user(request):
    following = request.user.following.all()
    return render(request,"users/following.html",{"following":following})