from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView



class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyAPIDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer