from django.urls import path
from .views import AboutList

app_name = 'about'


urlpatterns = [
    path('', AboutList.as_view(), name='about')
]
