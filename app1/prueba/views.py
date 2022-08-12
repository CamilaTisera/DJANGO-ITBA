from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'prueba/home.html')

def about(request):
    return render(request, 'about.html', {'data':data})



