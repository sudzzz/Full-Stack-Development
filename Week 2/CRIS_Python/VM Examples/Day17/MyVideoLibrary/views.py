from django.shortcuts import render
from django.http import HttpResponse
from MyVideoLibrary import models

# Create your views here.

def index(request):
    return HttpResponse("Welcome To Main Page")

#MyValues=["101","102","103","104"]
def Welcome(request):
    #MyCt={'MyVal' : MyValues}
    Obj=models.Employee
    MyCt={'MyVal' : Obj.RetValues("a")}
    return render(request,'Welcome.html',MyCt)

def Welcome_Save(request):
    res1=request.POST.get('UName',False)
    res2 = request.POST.get('UPwd', False)
    #model interaction
    return  HttpResponse(res1 + "-"  +res2)