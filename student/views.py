from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import student
# Create your views here.
class NewStudentView(CreateView):
    model = student
    fields = '__all__'


class ViewStudent(ListView):
    model = student
    fields='__all__'
    context_object_name = 'students'

