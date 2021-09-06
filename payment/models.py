from django.db import models
from addmission.models import addmission
from django.urls import reverse
# Create your models here.

class payment(models.Model):
    date=models.DateField()
    addmission=models.ForeignKey(addmission,on_delete=models.CASCADE,related_name='payment')
    ch=[('cash','cash'),('cheque','cheque'),('neft','neft')]
    type=models.CharField(max_length=25,choices=ch)
    amount=models.IntegerField()
    bank_name=models.CharField(max_length=40,blank=True,null=True)
    branch_name=models.CharField(max_length=40,blank=True,null=True)
    cheque_date=models.DateField(blank=True,null=True)
    cheque_no=models.CharField(max_length=50,blank=True,null=True)
    ref_id=models.CharField(max_length=40,blank=True,null=True)

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse('payment-view')

