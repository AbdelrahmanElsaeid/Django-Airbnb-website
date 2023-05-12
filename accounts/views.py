from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'accounts/profile.html', {'profile':profile })





def Signup(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            form.save()

            profile = Profile.objects.get(user__username=username)
            
    else:
        form = SignupForm()    

    return render(request, 'registration/signup.html', {'form':form})
