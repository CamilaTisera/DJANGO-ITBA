from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    num_visits = request.session.get{'num_visits',0}
    request.session{'num_visits'} = num_visits + 1
    context = {
        'num_visits':num_visits, 
    }
    return render(request, 'prueba/home.html' context=context)

def about(request):
    return render(request, 'prueba/about.html')



