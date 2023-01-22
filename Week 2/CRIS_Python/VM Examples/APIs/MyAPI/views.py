from django.shortcuts import render

from django.http import HttpResponse
import feedparser
# Create your views here.

def index(request):
    #feeds=feedparser.parse('https://johnsmallman.wordpress.com/author/johnsmallman/feed/')
    feeds = feedparser.parse('http://www.rssweather.com/wx/in/bombay/rss.php')

    str=""
    for f in feeds.entries:
        str+=(f.title) +"<br/>"

    return render(request,"index.html",{'v':str})