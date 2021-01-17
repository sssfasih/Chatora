from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import AuctionProduct
from .models import User,ProductCategory,Comment


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
    inWatchlist = False
    product = AuctionProduct.objects.get(id=id)
    if request.user.is_authenticated:
        if product in request.user.watchlist.all():
            inWatchlist = True
    # -- comments
    comments = product.comProduct.all()

    return render(request,"auctions/listing.html", {
        'product': product,
        'inWatchlist':inWatchlist,
        'comments': comments,
    })

def addComment(request,p_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text == '':
            return HttpResponseRedirect(reverse('listing',None,[p_id]))
        product= AuctionProduct.objects.get(pk=p_id)
        user = request.user
        com = Comment(commenter=user,text=text,prod_id=product)
        com.save()
        return HttpResponseRedirect(reverse('listing',None,[p_id]))

def closeAuction(request,id):
    if request.method=='POST':
        product = AuctionProduct.objects.get(id=id)
        if request.user == product.owner:
            product.active = False
            product.save()



        return HttpResponseRedirect(reverse('listing',None,[id]))

    else:
        print("GET")
        return HttpResponseRedirect(reverse('index'))


def watchlist(request):
    user = request.user
    #product.watchers.add(user)

    return render(request,'auctions/watchlist.html',{'watchlist':request.user.watchlist.all()})

def addWatch(request,p_id):
    product = AuctionProduct.objects.get(id=p_id)
    request.user.watchlist.add(product)
    return HttpResponseRedirect(reverse('watchlist'))

def removeWatch(request,p_id):
    product = AuctionProduct.objects.get(id=p_id)
    request.user.watchlist.remove(product)
    return HttpResponseRedirect(reverse('watchlist'))

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
