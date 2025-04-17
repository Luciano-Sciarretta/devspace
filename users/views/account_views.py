from django.shortcuts import render, redirect
from ..models import Profile
from django.contrib.auth.decorators import login_required
from ..forms import ProfileForm



@login_required(login_url='login')
def  user_account(request):
    profile = request.user.profile
    
    skills = profile.skill_set.all()
    
    projects = profile.project_set.all()
    context= {
        'profile':profile,
        'skills': skills,
        'projects': projects,
              }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {'form': form}
    return render(request, 'users/profile-form.html', context)

