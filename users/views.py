from django.shortcuts import render

def profiles(request):
    return render(request, "users/profiles.html")

def profile(request, pk):
    return render(request, "users/profile.html")