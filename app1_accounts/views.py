from django.shortcuts import render
from .models import Profile

def account_home(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'app1_accounts/account_home.html', {
        'user': request.user,
        'profile': profile
    })

from django.shortcuts import render

def landing_page(request):
    return render(request, 'home.html')
