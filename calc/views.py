from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html',{'val1':'val2'})
def sub(request):
   name1=request.GET["org"]
   
   return render(request, 'result.html',{'name':name1})
 