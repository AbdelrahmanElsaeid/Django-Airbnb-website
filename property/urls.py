from django.urls import path
from .views import PropertyList, PropertyDetail
from .api_view import PropertyAPIList, PropertyAPIDetail


app_name = 'property'


urlpatterns = [
    path('', PropertyList.as_view(),name='property_list'),
    path('<slug:slug>', PropertyDetail.as_view(),name='property_detail'),

    #---------------API-------------
    path('api/list' , PropertyAPIList.as_view(), name='property_list_api'),
    path('api/list/<int:pk>' , PropertyAPIDetail.as_view(), name='property_detail_api'),
    
]


