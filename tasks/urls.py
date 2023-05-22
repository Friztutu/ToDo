from django.urls import path
from tasks.views import IndexView, ListTasksView, NewTaskView, CardTaskView


app_name = 'tasks'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', ListTasksView.as_view(), name='list'),
    path('new/', NewTaskView.as_view(), name='new'),
    path('card/', CardTaskView.as_view(), name='card'),
]
