from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from .forms import (
    RegisterForm,
    AccountAuthenticationForm,
    AccountUpdateForm,
)
from .models import Account

def login_view(request):
    next = request.GET.get('next')
    user = request.user
    if user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You have already logged in')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    form = AccountAuthenticationForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You successfully have just loged in')
            if next:
                return redirect(next)
            return redirect('/')
    return render(request, 'pages/login.html', context={ 'form': form })

def register_view(request):
    next = request.GET.get('next')
    user = request.user
    if user.is_authenticated:
        messages.add_message(request, messages.INFO, 'You have already logged in')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    form = RegisterForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.add_message(request, messages.SUCCESS, f'You have successfully registered and logged into "{account.username.capitalize()}" account')
            messages.add_message(request, messages.INFO, 'New account has been created by You')
            if next:
                return redirect(next)
            return redirect('/')
    return render(request, 'pages/singup.html', context={ 'form': form })

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'You have successfully logged out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'pages/profile.html', context={ 'user': user })

@login_required
def edit_view(request):
    form = AccountUpdateForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully you have updated you account')
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = AccountUpdateForm(
            initial = {
                'email': request.user.email,
                'username': request.user.username
            }
        )

    return render(request, 'pages/edit.html', context={ 'form': form })