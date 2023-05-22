from django.views.generic.base import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class ListTasksView(TemplateView):
    template_name = 'tasks/main.html'


class NewTaskView(TemplateView):
    template_name = 'tasks/new.html'


class CardTaskView(TemplateView):
    template_name = 'tasks/card.html'
