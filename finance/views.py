from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def feeCollection(request):
    return render(request,'finance/feecollect.html')
    #return HttpResponse("<h1>I will collect fee</h1>")

def feeDuesReport(request):
    return HttpResponse("<h2>I will get fee due report</h2>")

def feeCollectionReport(request):
    return HttpResponse("<h2>I will get fee collection report</h2>")
