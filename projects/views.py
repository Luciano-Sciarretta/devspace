from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
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
            form.save()
            return redirect("user-account")
    
    context = {
        "form": form
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