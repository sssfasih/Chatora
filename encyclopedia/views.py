from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import markdown
from . import util
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    content = util.get_entry(title)
    if content == None:
        return HttpResponse("ERROR 404: Page does not exist")
    return render(request,"encyclopedia/entry.html",{'content':markdown(content),'title':title})

def search(request):
    query = request.GET.get('q').strip()
    result = util.get_entry(query)
    if result == None:
        MatchingEntries = []
        AllEntries = util.list_entries()
        for loop in AllEntries:
            if query in loop:
                MatchingEntries.append(loop)
        return render(request,'encyclopedia/search.html',{'entries':MatchingEntries})
    else:
        return render(request,'encyclopedia/entry.html',{'content':markdown(result)})

    return HttpResponse(query)

def createEntry(request):
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        content = request.POST.get('content').strip()
        if title == "" or content == "":
            return HttpResponse("Please fill all fields")
        if util.get_entry(title) != None:
            return HttpResponse("ERROR: Entry with that name already exists.")
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse('index'))

    return render(request,'encyclopedia/create.html',{'editMode':False,'title':None,"content":None})

def editEntry(request,title):
    validation = util.get_entry(title)
    if validation == None:
        return HttpResponse("ERROR 404: Page does not exist")
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse('entry',None,args=[title]))

    else:
        content = validation
        return render(request,"encyclopedia/create.html",{"editMode":True,'title':title,'content':content})

def randomPage(request):
    rand = choice(util.list_entries())

    return HttpResponseRedirect(reverse(entry,None,[rand]))