from django.shortcuts import render
from .models import Profile, Skill




def profiles(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, "users/profiles.html", context)


def profile(request, pk):
    profile = Profile.objects.get(id = pk)
   
    top_skills = profile.skills.exclude(description__exact="")
    other_skills = profile.skills.filter(description = "")
    context = {
        'profile': profile,
        "top_skills": top_skills,
        "other_skills": other_skills
    }
    return render(request, "users/user-profile.html", context)

    
    

    
