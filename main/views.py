from django.shortcuts import render
from .models import Competitor
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    competitors = Competitor.objects.all()
    return render(request, 'main/index.html', {'competitors': competitors})


def competitor_detail(request, pk):
    details = get_object_or_404(Competitor, pk=pk)
    return render(request, 'main/details.html', {'details': details})
