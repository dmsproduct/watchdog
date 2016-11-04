from django.shortcuts import render
from .models import Competitor


# Create your views here.
def index(request):
    competitors = Competitor.objects.all()
    return render(request, 'main/index.html', {'competitors': competitors})

