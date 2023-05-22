from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from tasks.models import Task
from django.urls import reverse_lazy
from tasks.forms import NewTaskForm


# Create your views here.

class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class ListTasksView(TemplateView):
    template_name = 'tasks/main.html'


class NewTaskView(CreateView):
    template_name = 'tasks/new.html'
    model = Task
    success_url = reverse_lazy('tasks:list')
    form_class = NewTaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardTaskView(TemplateView):
    template_name = 'tasks/card.html'
