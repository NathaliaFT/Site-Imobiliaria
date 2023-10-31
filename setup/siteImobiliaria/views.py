from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html') 

def contact(request):
    return render(request,'contact.html') 

def properties(request):
    return render(request,'properties.html') 

def property_details(request):
    return render(request,'property-details.html') 
