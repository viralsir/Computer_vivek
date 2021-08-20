from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from .models import addmission
# Create your views here.
class NewAddmissionView(CreateView):
    model = addmission
    fields = '__all__'


class ListAddmissionView(ListView):
    model = addmission
    context_object_name = 'addmissions'

class UpdateAddmissionView(UpdateView):
    model = addmission
    fields = '__all__'
class DeleteAddmissionView(DeleteView):
    model = addmission
    success_url = '/addmission/view'
class DetailAddmission(DetailView):
    model = addmission

