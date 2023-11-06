# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages   

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Rediriger vers la page d'accueil après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après la connexion
        else:
            # Ajoutez un message d'erreur si l'authentification échoue
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def home(request):
    user = request.user  # Récupérer l'utilisateur actuellement connecté
    return render(request, 'registration/home.html', {'user': user})