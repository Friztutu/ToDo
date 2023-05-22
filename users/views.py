from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView, CreateView
from users.models import CustomUser
from users.forms import LoginForm, ProfileForm, RegistrationForm
from django.http import HttpResponseRedirect


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')
    form_class = LoginForm

    def get_success_url(self):
        return reverse('users:profile', args=(self.request.user.id, ))


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    model = CustomUser
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:profile', args=(self.request.user.id, ))


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    model = CustomUser
    success_url = reverse_lazy('users:login')
    form_class = RegistrationForm
