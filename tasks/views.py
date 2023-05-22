from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from tasks.models import Task
from django.urls import reverse_lazy, reverse
from tasks.forms import NewTaskForm, EditTaskForm
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.

class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class ListTasksView(ListView):
    template_name = 'tasks/main.html'
    model = Task
    ordering = 'deadline'

    def get_queryset(self):
        progress = self.kwargs.get('progress')
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        queryset = Task.objects.filter(Q(title__icontains=query)) if query else queryset
        if not progress:
            queryset = queryset.filter(user_id=self.request.user.id, is_done=False, is_die=False)

        elif progress == 'die':
            queryset = queryset.filter(user_id=self.request.user.id, is_die=True, is_done=False)

        elif progress == 'done':
            queryset = queryset.filter(user_id=self.request.user.id, is_done=True)

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
        return reverse('tasks:card', args=(self.kwargs['pk'],))


def mark_task_as_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse('tasks:list'))


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect(reverse('tasks:list'))
