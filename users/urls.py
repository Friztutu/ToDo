from django.urls import path
from users.views import UserLoginView, ProfileView, RegistrationView, logout


app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout, name='logout')
]
