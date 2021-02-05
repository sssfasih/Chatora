from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import User, Post, Follow
import json


def index(request):
    all_posts = Post.objects.all().order_by('-created')

    r = request.GET.get('page')

    p = Paginator(all_posts,10)

    if r:
        page_posts = p.page(r)
    else:
        page_posts = p.page(1)

    return render(request, "network/index.html", {'posts': page_posts, 'paginator':p , 'title': "News Feed"})


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
    posts = Post.objects.filter(posted_by=requested_user).order_by('-created')

    #print(request.user,' != ',followers)
    fwers = []
    for loop in followers:
        fwers.append(loop.user.username)
    #print(fwers)

    return render(request, 'network/profile.html',
                  {'posts': posts, 'userx': requested_user, 'followers': fwers, 'following': following})


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

    r = request.GET.get('page')

    p = Paginator(posts_query_set, 10)

    if r:
        posts_query_set = p.page(r)
    else:
        posts_query_set = p.page(1)



    return render(request,'network/index.html',{'posts':posts_query_set,'title':"Favourites",'paginator':p})

@login_required
def follow(request,id):
    userx = User.objects.get(id=id)
    f_obj = Follow(user=request.user,following=userx)
    f_obj.save()
    return HttpResponseRedirect(reverse(view_profile,args=[id]))

@login_required
def unfollow(request,id):
    userx = User.objects.get(id=id)
    f_obj = Follow.objects.get(user=request.user,following=userx)
    f_obj.delete()
    return HttpResponseRedirect(reverse(view_profile,args=[id]))

@login_required
def edit(request,post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edited_text = data.get('editedText')
        if edited_text == "":
            return JsonResponse({'Done':False,'Updated':"ERROR: Back-End Received Empty Text"})
        post = Post.objects.get(pk=post_id)
        if request.user.username != post.posted_by:
            return JsonResponse({'Done': False, 'Updated': "ERROR: Trying to cheat system eh?"})

        post.text = edited_text
        post.save()

        return JsonResponse({'Done':True,'Updated':post.text})

    if request.method == "PUT":
        pass

    error = f"ERROR: '{request.method}' Route not Allowed"
    return HttpResponse(error)

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
