from django.shortcuts import render, redirect
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from ..forms import CustomUserCreationForm


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f"User { user.username } was successfully created!")
            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, "An error has occurred")
            
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)



def user_login(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect('profiles')

        else:
            messages.error(request, "Username or password is incorrect")
    context = {
        'page': page
    }
    return render(request, 'users/login_register.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, "User was successfully logout")
    return redirect('login')