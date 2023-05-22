from django.urls import path
from tasks.views import IndexView, ListTasksView, NewTaskView, CardTaskView, delete_task, mark_task_as_complete
from django.contrib.auth.decorators import login_required


app_name = 'tasks'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', login_required(ListTasksView.as_view()), name='list'),
    path('list/<slug:progress>/', login_required(ListTasksView.as_view()), name='list_filter'),
    path('new/', login_required(NewTaskView.as_view()), name='new'),
    path('card/<int:pk>/', login_required(CardTaskView.as_view()), name='card'),
    path('delete/<slug:pk>/', login_required(delete_task), name='delete'),
    path('complete/<slug:pk>/', login_required(mark_task_as_complete), name='complete'),
]
