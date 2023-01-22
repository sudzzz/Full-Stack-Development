from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def welcome(request):
    return render(request,"welcome.html")

def aboutus(request):
    return render(request,"aboutus.html")

def aboutus2(request):
    return render(request,"aboutus2.html")
