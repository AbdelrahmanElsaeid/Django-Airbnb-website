from django.urls import path
from .views import Home ,home_search, category_filter

app_name = 'settings'

urlpatterns = [
    path('' , Home,name='home'),
    path('search' , home_search,name='home_search'),
    path('category/<slug:category>' ,category_filter ,name='category_filter'),


]    