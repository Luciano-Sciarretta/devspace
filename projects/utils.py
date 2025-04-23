from django.db.models import Q
from projects.models import Project



def searchProjects(request):
    search_query = ""
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()
        
        if search_query:
            projects = Project.objects.filter(Q(title__icontains = search_query) | Q(owner__name__icontains= search_query) | Q(tags__name__icontains = search_query)).distinct()
       
    else:
        projects = Project.objects.all()
        
    return  search_query, projects