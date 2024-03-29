from allauth.account.forms import LoginForm
from allauth.account.views import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login/'
    template_name = 'registration/signup.html'

#
# def sign_in(request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect('posts')
#
#         form = LoginForm()
#         return render(request, 'users/login.html', {'form': form})
#
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 messages.success(request, f'Hi {username.title()}, welcome back!')
#                 return redirect('posts')
#
#         # either form not valid or user is not authenticated
#         messages.error(request, f'Invalid username or password')
#         return render(request, 'users/login.html', {'form': form})
#
#
# def sign_out(request):
#     logout(request)
#     messages.success(request, f'You have been logged out.')
#     return redirect('login')


