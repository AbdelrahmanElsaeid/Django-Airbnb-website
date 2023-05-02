from django.shortcuts import render
from .models import Settings
# Create your views here.


def Home(request):

    return render(request, 'settings/home.html', {})
