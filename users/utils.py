from django.db.models import Q
from users.models import Profile


def searchProfiles(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()
        
    
    if search_query:
        profiles = Profile.objects.filter(
        Q(name__icontains=search_query) |
        Q(skill__name__iexact=search_query)  #Sintaxis específica de la API de consultas de Django.
).distinct()    
        
    else:
        profiles = Profile.objects.all()
        
    return profiles, search_query
