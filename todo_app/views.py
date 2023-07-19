from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.all().order_by("-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:home-page")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:home-page")
    form_class = TaskForm


class TaskStatusUpdateView(generic.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse("todo:home-page"))


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home-page")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
