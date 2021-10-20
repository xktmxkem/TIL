from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)