from django.shortcuts import render, HttpResponse
from models import get_data

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    data = get_data()
    return render(request, 'about.html')



