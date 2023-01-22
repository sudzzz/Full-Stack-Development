from django.shortcuts import render
from django.http import HttpResponse
from MyApp import models

# Create your views here.
def index(request):
    MyD=models.MyDatabase()
    MyD.createTable()

    return render(request,'index.html')

def CustomerSave(request):
    v1 = request.POST.get('code',False)
    v2 = request.POST.get('name', False)
    v3 = request.POST.get('street', False)
    v4 = request.POST.get('balance', False)
    MyD=models.MyDatabase()
    MyD.addCust(v1,v2,v3,v4)
    return render(request,'index.html')

def ShowData(request):
    MyD=models.MyDatabase()
    str=""
    for k in MyD.ReadCust():
        str+=("<tr><td>"+ k +"</td></tr>")

    return HttpResponse("<table " + str + "</table>")

def ShowData2(request):
    MyD=models.MyDatabase()
    Lst={'nm':MyD.ReadCust2()}

    return render(request,"ShowResult.html",Lst)

def test(request):

    return render(request,"test.html",{'un':"Harmeet"})


def test2(request):
    MyD=models.MyDatabase()
    Lst={'nm':MyD.ReadIds()}

    return render(request,"test2.html",Lst)

def test_ajax_script(request):

    Lst={'nm':request.GET['cd']}
    str = ""
    for k in Lst:
        str += ("<tr><td>" + k + "</td></tr>")

    return HttpResponse(str)



def sessiontest(request):
    return render(request,"sessiontest.html")

def sessiontest2(request):
    un=request.POST.get('uname')
    #request.COOKIES["CookiesUN"]=un
    request.session["SessionUN"] = un
    #return HttpResponse(request.COOKIES["CookiesUN"])
    return HttpResponse(request.session["SessionUN"])