from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'myapp/templates/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapp/templates/task_create.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'myapp/templates/task_update.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapp/templates/task_delete.html'
    success_url = reverse_lazy('task_list')
