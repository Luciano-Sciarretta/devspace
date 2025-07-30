from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse, JsonResponse
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, projects_pagination
from django.contrib import messages



def projects(request):
    search_query, projects = searchProjects(request)
    custom_range, projects = projects_pagination(request, projects, 6)
    

    context = {
        'projects': projects, #Cuando itero en el template django internamente aplica el método objects_list. Por eso puedo mostrar los projects
        'search_query': search_query,
        'custom_range': custom_range, 
         
    }
    return render(request, "projects/projects.html", context)



def project(request, pk):
    project = Project.objects.get(id = pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.get_vote_count
        messages.success(request, f"Your review for {project.title} was successfully submitted!")
        return redirect('project', project.id)
     
    context = {
        "project": project,
        'form': form
        }
    return render(request, "projects/single-project.html", context)




@login_required(login_url='login')
def create_project(request):
    
    
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            
            tags_list = form.cleaned_data['tags']
            for tag in tags_list:
                tag, created = Tag.objects.get_or_create(name = tag)
                project.tags.add(tag)
            
            return redirect("user-account")
              
    context = {
        "form": form
    }
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def update_project(request, pk):
   

    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance = project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            
            tags_list = form.cleaned_data['tags']
            current_tags = project.tags.values_list('name',  flat=True)
            print("Current tags:",  current_tags)
            
            for tag in tags_list:
                if tag not in current_tags:
                    tag_obj, created = Tag.objects.get_or_create(name = tag)
                    # print("Tag en  for: ", tag, created)
                    project.tags.add(tag_obj)
            form.save()
            return redirect("user-account")
    
    context = {
        "form": form,
        'project': project,
    }
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
        
    context = {
        "object": project
    }
    return render(request, "delete-template.html", context)

@login_required(login_url='login')
def remove_tag(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            tag_id = data['tag_id']
            project_id = data['project_id']
            # print( "\n","tag id:", tag_id, "\n","project_id:", project_id, "\n")
            tag = Tag.objects.get(id = tag_id)
            project = Project.objects.get(id = project_id)
            print("Project:", project, "tag:", tag)
            project.tags.remove(tag)
            return JsonResponse({
                "message": "Tag removed successfully",
                "tag_id": tag_id,
                "project_id": project_id
                }, status = 200)
        
        except Exception as e:
            print(f"Error inesperado: {type(e)} - {e}")
            return JsonResponse({"error": "Error inesperado"}, status=500)
        
                
    