from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

from .forms import AddWorker
from .models import Worker, OccupationAgeAvg

class WorkersList(ListView):
    template_name = 'workers_app/main.html'
    model = Worker
    context_object_name = 'workers'


class WorkerDetails(DetailView):
    template_name = 'workers_app/worker_details.html'
    model = Worker
    pk_url_kwarg = 'worker_pk'



class WorkerCreate(FormView):
    template_name = 'workers_app/add_worker.html'
    form_class = AddWorker
    success_url = reverse_lazy('workers-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WorkerUpdate(UpdateView):
    template_name = 'workers_app/update_worker.html'
    model = Worker
    form_class = AddWorker
    pk_url_kwarg = 'worker_pk'
    success_url = reverse_lazy('workers-list')
    

class WorkerDelete(View):
    def get(self, request, *args, **kwargs):
        worker = Worker.objects.get(pk=kwargs['worker_pk'])
        worker.delete()
        return redirect('workers-list')


class OccupationAgeAvgReport(ListView):
    template_name='workers_app/age_report.html'
    model = OccupationAgeAvg
    context_object_name = 'occupations'