from django.contrib.auth.decorators import login_required
from django.urls import path
from start_pages.views import IndexView

app_name = 'start_pages'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
