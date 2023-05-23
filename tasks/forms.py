from django import forms
from tasks.models import Task


class NewTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'datetime', 'type': 'datetime-local'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 20em;'}))

    class Meta:
        model = Task
        fields = ('title', 'deadline', 'description')


class EditTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'datetime', 'type': 'datetime-local'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 20em;'}))

    class Meta:
        model = Task
        fields = ('title', 'deadline', 'description')
