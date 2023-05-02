from .models import Settings




def Myfooter(request):
    myfooter = Settings.objects.last()

    return {'myfooter':myfooter}