from django.shortcuts import render

# Create your views here.

#view é um objeto chamavel que recebe uma httprequest e retorna uma httpresponse

def home(request):
    #render processa uma request e retorna um template
    return render(request, 'index.html')