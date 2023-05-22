from django.urls import path
from tasks.views import IndexView, ListTasksView, NewTaskView, CardTaskView
from django.contrib.auth.decorators import login_required


app_name = 'tasks'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', login_required(ListTasksView.as_view()), name='list'),
    path('new/', login_required(NewTaskView.as_view()), name='new'),
    path('card/<int:pk>/', login_required(CardTaskView.as_view()), name='card'),
]
