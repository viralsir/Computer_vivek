from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import course
# Create your views here.

class NewCourseView(CreateView):
    model = course
    fields = '__all__'

# model_form.html
#course_form.html

class ListCourseView(ListView):
    model = course
    context_object_name = 'courses'
#model_list.html

class UpdateCourseView(UpdateView):
    model = course
    fields = '__all__'

#model_form.html

class DeleteCourseView(DeleteView):
    model = course
    success_url = "/course/view"

#model_confirm_delete.html