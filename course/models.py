from django.db import models
from django.urls import reverse
# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField(blank=True,null=True)
    durations=models.IntegerField()
    fees=models.IntegerField()
    ch=[('Active','Active'),('Deactive','Deactive')]
    status=models.CharField(max_length=50,choices=ch)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('course-view')