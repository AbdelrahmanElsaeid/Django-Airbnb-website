from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property
# Create your views here.



class PropertyList(ListView):
    model = Property
    paginate_by = 1





class PropertyDetail(DetailView):
    model = Property