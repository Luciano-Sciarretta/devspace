from django.shortcuts import render, redirect
from ..models import Skill
from django.contrib.auth.decorators import login_required
from ..forms import SkillForm
from django.contrib import messages



login_required(login_url='login')
def create_skill(request):
    form = SkillForm()
    profile = request.user.profile
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was created successfully!')
            return redirect('user-account')
        else:
            messages.error(request, 'An error has occurred')
    
    context = {'form': form}
    return render(request, 'users/skill-form.html', context)


login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance = skill)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance= skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('user-account')
        else:
            messages.error(request, 'An error has occurred')
    
    context = {'form': form}
    return render(request, 'users/skill-form.html', context)


def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'The skill has been deleted successfully!')
        return redirect('user-account')
        
    context = {'object': skill}
    return render(request, 'delete-template.html', context)