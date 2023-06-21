from django.contrib.auth.decorators import login_required
from django.urls import path
from users.views import ProfileView, LoginView, RegistrationView

app_name = 'users'


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
