from django.shortcuts import render
from django.http import HttpResponse
from .fake_information import fake


def projects(request):
    
    context = {
        'projects': fake,
        
    }
    return render(request, "projects/projects.html", context)

def project(request, pk):
    project = None
    for i in fake:
        if i["id"] == pk:
            project = i
    context = {
        "pk": pk,
        "project": project
        }
    
    return render(request, "projects/project.html", context)
