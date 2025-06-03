from django.db.models import Q
from projects.models import Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#Barra de búsqueda
def searchProjects(request):
    search_query = ""
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()
        
        if search_query:
            projects = Project.objects.filter(Q(title__icontains = search_query) | Q(owner__name__icontains= search_query) | Q(tags__name__icontains = search_query)).distinct()
       
    else:
        projects = Project.objects.all()
        
    return  search_query, projects

#Paginación

def projects_pagination(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)
    
    try:
        projects = paginator.page(page) # Objeto page que tiene x objetos por página
        
    except PageNotAnInteger:  # cuando la url después del path no tiene parámetro de consulta o el parámetro no es de tipo integer
        page = 1
        projects = paginator.page(page)
        
    except EmptyPage:    # cuando se solicita una página que no existe (fuera del rango de páginas disponibles)
        page = paginator.num_pages  
        projects = paginator.page(page)
        
    current_page = projects.number 
    total_pages = paginator.num_pages
    left_index = current_page - 2 
    if left_index < 1:
        left_index = 1

    right_index = left_index + 5  
    if right_index > total_pages + 1:
        right_index = total_pages + 1
        left_index = max(1, right_index - 5)  # Ajustar para mantener 5 botones

    custom_range = range(left_index, right_index)
    
    return custom_range, projects