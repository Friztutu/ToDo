from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from users.models import CustomUser
from users.forms import UserLoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse('users:profile', args=(self.request.user.id,))


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    model = CustomUser

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    model = CustomUser
    success_url = reverse_lazy('users:login')
    form_class = RegistrationForm


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('start_pages:index'))
