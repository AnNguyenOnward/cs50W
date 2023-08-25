from django.shortcuts import render,redirect
from . import util
from django.http import HttpResponseRedirect
import markdown2
import random
from django.http import HttpResponse
from django import forms
from django.urls import reverse
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def newPage(request):
    return render(request,"encyclopedia/new_page.html")
def visitPage(request,page_name):
    return render(request,"encyclopedia/page.html",{
        "page_name" : page_name,
        "page_content" : markdown2.markdown(util.get_entry(page_name))
    })
def randomPage(request):
    pages = util.list_entries()
    random_page_num = random.randint(0,len(pages) - 1)
    return HttpResponseRedirect(f"wiki/{pages[random_page_num]}")
def search(request):
    if request.method == "GET":
        matched_entries = []
        form = request.GET
        searched = form['q']
        for entry in util.list_entries():
            if searched.lower() in entry.lower():
                matched_entries.append(entry)
        return render(request,"encyclopedia/search.html",{
            "matched_entries" : matched_entries
        })
    else:
        return HttpResponse(request.method)
def add(request):
    form = request.POST
    title = form['title']
    content = form['content']
    util.save_entry(title, content)
    return HttpResponseRedirect(f"wiki/{title}")
def editPage(request,page_name):
    content = util.get_entry(page_name)
    if request.method == "POST":
        form = request.POST
        content = form['content']
        util.save_entry(page_name,content)
        return redirect("page",page_name)

    else:
        return render(request,"encyclopedia/edit.html",{
            "page_name":page_name,
            "content":content
        })