from django.shortcuts import render
from ..models import Profile
from ..utils import searchProfiles, profiles_pagination




def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = profiles_pagination(request, profiles, 6)
    
    context = {
        "profiles": profiles,
        "search_query": search_query,
        "custom_range": custom_range,
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

    
    

    
