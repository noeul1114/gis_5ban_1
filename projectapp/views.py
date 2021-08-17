from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'


