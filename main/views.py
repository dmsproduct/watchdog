from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return(request, 'main/index.html', context)

