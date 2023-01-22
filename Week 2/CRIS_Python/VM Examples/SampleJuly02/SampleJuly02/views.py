from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from SampleJuly02.models import *

def index(request):
    return HttpResponse("<h1>Welcome</h1>")

def SecondSave(request):
    v=request.POST.get('txtName',False)
    #Models---db
    return HttpResponse("<h1>" + str(v) + "</h1>")

Lst=["indi",'ausi']
def Second(request):
        ctx = {'lst': Lst}
        '''tmp=loader.get_template('Second.html');

        return HttpResponse(tmp.render(ctx,request))'''
        return render(request, 'Second.html', ctx)





