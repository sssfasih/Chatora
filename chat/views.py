from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import User,Message,Conversation
import json

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('messages'))

def new_msg(request):
    return render(request,'chat/new_msg.html')

def messages(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("index"))
    user = request.user
    conv_id = request.GET.get('conv_id')

    con = Conversation.objects.filter(participants=user).order_by('-Last_Updated')
    if conv_id == "" or conv_id == None:
        try:
            latest = con[0].id
        except IndexError:
            latest = ""
    else:
        try:
            latest = int(conv_id)
        except ValueError:
            latest = ""

    if type(latest) is int:
        disp_msgs = Conversation.objects.get(pk=latest).Messages.order_by('id')
        disp_conv = disp_msgs.first().texts.get()
        if request.user not in disp_conv.participants.all():
            disp_conv = None
            disp_msgs = None
    else:
        disp_msgs = None



    return render(request,'chat/messages.html',{'all_conversations':con,'disp_msgs':disp_msgs,'disp_conv':disp_conv})

@login_required
def send_message(request,convo_id):
    if request.method == "PUT":

        data = json.loads(request.body)
        if not str(convo_id) == data['convoID']:
            return JsonResponse({'Done':False})
        conv = Conversation.objects.get(pk=convo_id)
        if request.user not in conv.participants.all():
            return JsonResponse({'Done':False,'ERROR':'User trying to send msg in foreign conversation.'})
        newMsg = Message(From=request.user,Text=data['txt'])
        newMsg.save()
        conv.Messages.add(newMsg)
        conv.save()


        return JsonResponse({'Done':True,'up_txt': newMsg.Text, 'up_ConvoID': conv.id})

    return HttpResponseRedirect(reverse('index'))

@login_required
def get_updates(request):

    if request.method == "POST":
        user = request.user
        updates = {}
        cons = Conversation.objects.filter(participants=user)
        for eachCon in cons:
            lastMsg = eachCon.Messages.last()
            if user not in lastMsg.Read_by.all():
                #lastMsg.Read_by.add(user)
                updates[eachCon.id]= lastMsg.Text

                print("last msg not seen by user")
        print(updates)
        return JsonResponse(updates, safe=False)

    elif request.method == "PUT":
        print("PUT Request")
        data = json.loads(request.body)
        try:
            convo_id = int(data['disp'])
            convo = Conversation.objects.get(pk=convo_id)
            if request.user not in convo.participants.all():
                JsonResponse(['ERROR: Frontend sent wrong convo id'],safe=False)
            new_msgs = []
            msgs = convo.Messages.exclude(Read_by=request.user)
            for loop in msgs:
                new_msgs.append([loop.Text,loop.From.id])
                loop.Read_by.add(request.user)
        except:
            new_msgs = ["No new message"]

        return JsonResponse(new_msgs,safe=False)

    return HttpResponseRedirect(reverse('index'))


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
            return render(request, "chat/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "chat/login.html")


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
            return render(request, "chat/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=name)
            user.save()
        except IntegrityError:
            return render(request, "chat/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "chat/register.html")
