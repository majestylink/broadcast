from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import SignUpForm
from core.models import Playlist


class SignUpView(View):

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index_page')
        return render(request, 'broadcast/register.html')

    def post(self, request, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Valid form")
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            if user is not None:
                return redirect('core:index_page')
            else:
                return render(request, 'broadcast/login.html')
        else:
            print("Invalid form")
            print(form.errors)
            messages.error(request, form.errors)
            return redirect('accounts:sign-up')


class LogOutView(View):
    def get(self, request, **kwargs):
        logout(request)
        return redirect('core:index_page')


class LoginView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in')
            return redirect('core:index_page')
        else:
            return render(request, 'broadcast/login.html', {})

    @staticmethod
    def post(request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            if user.is_active:
                return redirect('core:index_page')
            else:
                messages.error(request, 'Your account has been disabled')
                return render(request, 'broadcast/login.html')
        elif user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
        else:
            return redirect('accounts:login')


class ProfileView(View):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        else:
            user = request.user
            playlist = Playlist.objects.filter(user=request.user)
            return render(request, 'broadcast/profile.html', {'user': user, 'playlist': playlist})

    # @staticmethod
    # def post(request):
    #     data = request.POST
    #     username = data.get('username')
    #     password = data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    #     if user is not None:
    #         if user.is_active:
    #             return redirect('core:index_page')
    #         else:
    #             messages.error(request, 'Your account has been disabled')
    #             return render(request, 'broadcast/login.html')
    #     elif user is None:
    #         messages.error(request, 'Invalid credentials')
    #         return redirect('accounts:login')
    #     else:
    #         return redirect('accounts:login')
