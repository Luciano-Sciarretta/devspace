from django.db.models import Q
from users.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def profiles_pagination(request, profiles, results):
    page = request.GET.get('page', 1)
    try:
        page = int(page)  # Convertimos a entero
    except (ValueError, TypeError):  # Si no se puede convertir
        page = 1
    
    paginator = Paginator(profiles, results)
    # print('paginatoor fuera try:', paginator)
    try:
        profiles = paginator.page(page)
        # print('profiles:::', type(profiles))
        # print('profiles en try:', profiles.object_list)
    except PageNotAnInteger as e:  # cuando la url después del path no tiene parámetro de consulta o el parámetro no es de tipo integer
        print("PageNotAnInteger >>>", e)
        page = 1
        profiles = paginator.page(page)
        
    except EmptyPage as e:    # cuando se solicita una página que no existe (fuera del rango de páginas disponibles)
        
        print("EmptyPage >>>", e)
        page = paginator.num_pages  #num_pages es la cantidad de páginas actual.
        profiles = paginator.page(page)
        
    except Exception as e:
        import traceback
        print("ERROR inesperado en paginator:", e)
        traceback.print_exc()
        raise    
        
        
    current_page = profiles.number 
    total_pages = paginator.num_pages
    left_index = current_page - 2 
    if left_index < 1:
        left_index = 1

    right_index = left_index + 5  
    if right_index > total_pages + 1:
        right_index = total_pages + 1
        left_index = max(1, right_index - 5)  # Ajustar para mantener 5 botones

    custom_range = range(left_index, right_index)
    
    return custom_range, profiles