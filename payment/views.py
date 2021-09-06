from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView,ListView
from .models import payment
# Create your views here.
class NewPayment(CreateView):
    model = payment
    fields = '__all__' #['','']
class ViewPayment(ListView):
    model = payment
    fields = '__all__'
    context_object_name = 'payments'

class UpdatePayment(UpdateView):
    model = payment
    fields='__all__'

class DeletePayment(DeleteView):
    model = payment
    success_url = '/payment/view'