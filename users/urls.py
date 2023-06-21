from django.contrib.auth.decorators import login_required
from django.urls import path
from users.views import ProfileView, UserLoginView, RegistrationView

app_name = 'users'


urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
