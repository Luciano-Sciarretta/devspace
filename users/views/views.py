from django.shortcuts import render
from ..models import Profile
from ..utils import searchProfiles



def profiles(request):
    profiles, search_query = searchProfiles(request)

    context = {
        "profiles": profiles,
        'search_query': search_query,
    }
    return render(request, "users/profiles.html", context)


def profile(request, pk):
    profile = Profile.objects.get(id = pk)
   
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description = "")
    context = {
        'profile': profile,
        "top_skills": top_skills,
        "other_skills": other_skills
    }
    return render(request, "users/user-profile.html", context)

    
    

    
