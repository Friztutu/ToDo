from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from tasks.models import Task
from django.urls import reverse_lazy, reverse
from tasks.forms import NewTaskForm, EditTaskForm


# Create your views here.

class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class ListTasksView(ListView):
    template_name = 'tasks/main.html'
    model = Task
    ordering = 'deadline'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset


class NewTaskView(CreateView):
    template_name = 'tasks/new.html'
    model = Task
    success_url = reverse_lazy('tasks:list')
    form_class = NewTaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardTaskView(UpdateView):
    template_name = 'tasks/card.html'
    model = Task
    form_class = EditTaskForm

    def get_success_url(self):
        return reverse('tasks:card', args=(self.kwargs['pk'], ))
