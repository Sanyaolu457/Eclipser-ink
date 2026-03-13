from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from .forms import UserRegistration, UserLogin


def register_view(request):
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
           user = form.save() 
           login(request, user, backend='django.contrib.auth.backends.ModelBackend')
           messages.success(request, f'Account Created Succesfully! Welcome!', extra_tags='toast')
           
           if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
           return redirect('home')

        else:
            messages.error(request, f'please correct the error below!', extra_tags= 'toast')
    
    else:
        form = UserRegistration()

    return render (request, 'register.html', {
        'form': form
    })

def login_view(request):

    if request.method == 'POST':
        form = UserLogin(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()

            if user is not None:
                login(request, user)
                # messages.success(request, f'Welcome back, {user.username}!', extra_tags='toast')

                next_url = request.GET.get('next')

                if next_url:
                    return redirect (next_url)
                return redirect('home')
            
        else:
            messages.error(request, f'Invalid Username or Incorrect Password!')

    else:
        form = UserLogin()

    return render (request, 'login.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    messages.info(request, f'Logout Succesfully')
    return redirect('login')