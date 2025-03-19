from django.shortcuts import render
from ..models import Profile
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def  user_account(request):
    profile = request.user.profile
    skills = profile.skills.all()
    projects = profile.project_set.all()
    context= {
        'profile':profile,
        'skills': skills,
        'projects': projects,
              }
    return render(request, 'users/account.html', context)

