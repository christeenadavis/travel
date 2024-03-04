from django.http import Httpresponse
from django.shortcuts import render
# Create your views here.


def part(request):
    name="Kerala"
 return render(request,"about.html",{'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
return render(request,"result.html",{'result':res})
def multiplication(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res = x * y
return render(request,"result.html",{'result':res})
def division(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res= x / y
return render(request,"result.html",{'result':res})
def substraction(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res = x - y
return render(request,"result.html",{'result':res})

