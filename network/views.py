from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Post, Follow


def index(request):
    all_posts = Post.objects.all()

    return render(request, "network/index.html", {'posts': all_posts, 'title': "News Feed"})


@login_required
def create(request):
    if request.method == 'POST':
        text = request.POST.get('post_text')
        user = request.user
        p = Post(posted_by=user, text=text)
        p.save()
    return HttpResponseRedirect(reverse('index'))


def view_profile(request, id):
    requested_user = User.objects.get(pk=id)
    following = Follow.objects.filter(user=requested_user)
    followers = Follow.objects.filter(following=requested_user)
    posts = Post.objects.filter(posted_by=requested_user)

    return render(request, 'network/profile.html',
                  {'posts': posts, 'userx': requested_user, 'followers': followers, 'following': following})


@login_required
def favourites(request):
    user = request.user
    # from user object we are using reverse foreign key user of Follow class.
    follow_objs = Follow.objects.filter(user=user)

    users = []
    for loop in follow_objs:
        users.append(loop.following)

    # __in makes can take iterable objects
    posts_query_set = Post.objects.filter(posted_by__in=users)

    #print("**********")
    #print(posts_query_set)
    #print("**********")

    return render(request,'network/index.html',{'posts':posts_query_set,'title':"Favourites"})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        name = request.POST["Name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=name)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
