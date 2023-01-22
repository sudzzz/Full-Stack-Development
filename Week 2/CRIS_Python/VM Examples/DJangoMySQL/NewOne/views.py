from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from NewOne import models

# Create your views here.
def index(request):
    CustObj=models.Customer()
    return HttpResponse("Done")

def result(request):
    CustObj=models.Customer()
    Lst={'Info':CustObj.ReadCustomers()}
    return render(request,'result.html',Lst)

def resultJSON2(request):
    CustObj = models.Customer()

    return JsonResponse(CustObj.ReadCustomers(),safe=False)

def resultJSON(request):
    return JsonResponse([{"country": "USA","visits": 4025,"color": "#FF0F00"},
{"country": "India","visits": 2222,"color": "Yellow"},
],safe=False)
