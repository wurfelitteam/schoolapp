from django.shortcuts import render
#from django.http import HttpResponse
from admissions.models import student

# Create your views here.
#request is just a variable name. you can give anything over there."A"

def homepage(request):
    return render(request,'index.html')

def addAdmission(request):
    outvalues = {"name":"Adithya","Age":32,"Address":"Bangalore"}
    return render(request,'admissions/addadmission.html',outvalues)
    #return HttpResponse("<h1>This is add admission view</h1>")

def admissionReport(request):
    result = student.objects.all()#select * from students
    studdents = {"allstudents":result}

    return render(request,'admissions/admissionreports.html',studdents)
