from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(request):
    s='harsha'
    return render(request,'base.html',{'s':s})
