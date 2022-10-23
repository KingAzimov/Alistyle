from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user=authenticate(username=request.POST.get('l'),
                          password=request.POST.get('p'))
        if user is None:
            return redirect('/login/')
        login(request, user)
        return redirect('/')

class LogoutView(View):
    def get(self, request):
        return redirect('/login/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
