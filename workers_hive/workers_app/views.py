from django.views.generic import ListView
from django.shortcuts import render
from django.views import View

from .models import Worker

class WorkersList(ListView):
    template_name = 'workers_app/main.html'
    model = Worker
    context_object_name = 'workers'

class WorkerDetails(View):
    pass

class WorkerCreate(View):
    pass

class WorkerUpdate(View):
    pass

class WorkerDelete(View):
    pass
