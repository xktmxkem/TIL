from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')