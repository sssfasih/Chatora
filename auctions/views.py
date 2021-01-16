from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import AuctionProduct
from .models import User,ProductCategory


def index(request):
    allProds = AuctionProduct.objects.filter(active=True)

    return render(request, "auctions/index.html", context={
        'products':allProds,

    })


def create(request):
    if request.method == "POST":
        name = request.POST.get('p_name')
        desc = request.POST.get('desc')
        cat = request.POST.get('cat')
        catObj = ProductCategory.objects.get(category=cat)
        init_price = int(request.POST.get('init_price'))
        img = request.POST.get('img')
        owner = request.user
        obj = AuctionProduct(name=name,image=img,desc=desc,cat_id=catObj,owner=owner,highest=init_price)
        obj.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        allCats = ProductCategory.objects.all()
        return render(request,'auctions/create.html',context={
            'categories': allCats

        })

def listing(request,id):
    print("***********")
    print(id)
    product = AuctionProduct.objects.get(id=id)
    print(product.name)
    print("***********")

#    return HttpResponse("<h1>Testing</h1>")
    return render(request,"auctions/listing.html", {
        'product': product
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
