from django.shortcuts import render
from .models import Settings
from property.models import Property,Place,Category
from django.db.models.query_utils import Q

# Create your views here.


def Home(request):
    place = Place.objects.all()
    categories = Category.objects.all()

    return render(request, 'settings/home.html', {'places':place,'category':categories})



def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    property_list = Property.objects.filter(
        Q(name__icontains = name) &
        Q(place__name__icontains=place)

    )
    return render(request, 'settings/home_search.html', {'property_list':property_list})


def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(Category=category)
    return render(request, 'settings/home_search.html', {'property_list':property_list})