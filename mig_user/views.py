from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        form = RegistrationForm(initial={'is_staff': True})
    return render(request, 'mig_user/register.html', {'form': form})


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = User.objects.get(username=username, password=password)
            except Exception:
                return redirect('index')  # login error
            if user is not None:
                if user.is_staff:
                    return redirect('staff')
                else:
                    return redirect('user')
            else:
                return redirect('index')  # login error
    else:
        form = LoginForm()
    return render(request, 'mig_user/index.html', {'form': form})


def user(request):
    return render(request, 'mig_user/user.html')


def staff(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'mig_user/staff.html', {'form': form})
