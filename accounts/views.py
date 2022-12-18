from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def signUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, '../templates/accounts/signup.html', {'form': form})


def logInView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, '../templates/accounts/login.html', {'form': form})


def logOutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
