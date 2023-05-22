from django.shortcuts import render
from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    template_name = 'users/login.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class RegistrationView(TemplateView):
    template_name = 'users/register.html'
