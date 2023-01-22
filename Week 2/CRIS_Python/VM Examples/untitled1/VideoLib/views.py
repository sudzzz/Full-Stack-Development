from django.shortcuts import render
from django.http import HttpResponse
from VideoLib import models
from django.http import JsonResponse

# Create your views here.

def index(request):
    MyD=models.MyDatabase()
    #MyD.createDb()
    MyD.createTable()

    return render(request, 'index.html')


def indexProcess(request):
    val1=request.POST.get('name',False)
    val2= request.POST.get('street', False)
    val3 = request.POST.get('balance', False)
    val0 = request.POST.get('code', False)
    MyD = models.MyDatabase()
    MyD.addCust(val0,val1,val2,val3)

    return render(request, 'index.html')

def indexResult(request):
    MyD=models.MyDatabase()
    #MyD.createDb()
    #Lst={'nm',MyD.readCust()}
    str=""
    for k in MyD.readCust():
        str+=("<tr><td>%s</td></tr>" % (k))

    return HttpResponse("<table border='1'>"+str+"</table>")
    #return render(request, 'indexResult.html',Lst)

def indexResult2(request):
    MyD=models.MyDatabase()
    #MyD.createDb()
    Lst={'nm':MyD.readCust2()}
    #str=""
    #for k in MyD.readCust():
    #    str+=("<tr><td>%s</td></tr>" % (k))

    #return HttpResponse("<table border='1'>"+str+"</table>")
    return render(request, 'indexResult.html',Lst)

def indexDelete(request):
    MyD=models.MyDatabase()
    MyD.delCust()
    return HttpResponse("Table Empty")

def pie3D(request):
    return render(request, 'pie3D.html')


def pie3D_ajax_script(request):
    MyD=models.MyDatabase()
    return JsonResponse(MyD.MyPieData(),safe=False)

def pie3D_ajax_script_smart(request):
    #MyD = models.MyDatabase()

    str="["
    #for k in MyD.MyPieData():
    str+=("{'TName':'India','TValue' : 2000},{'TName':'Australia','TValue' : 1800}")
    str+="]"

    return HttpResponse(str)


def testsession(request):
    Lst = {'UName': 'Harmeet'}
    return render(request,'testsession.html',Lst)

def testsession2(request):

    return render(request,'testsession2.html')