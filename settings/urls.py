from django.urls import path
from .views import Home

app_name = 'settings'

urlpatterns = [
    path('' , Home,name='home'),


]    