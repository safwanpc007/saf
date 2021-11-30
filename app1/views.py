from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'html.html')
# def one(request):
#     return render(request,'html.html')Pr