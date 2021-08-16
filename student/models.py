from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    father_first_name = models.CharField(max_length=50)
    father_last_name = models.CharField(max_length=50)
    father_middle_name = models.CharField(max_length=50)
    street=models.CharField(max_length=200)
    areaname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    phno1=models.CharField(max_length=10)
    phno2=models.CharField(max_length=10)
    birth_date=models.DateField()
    gender=models.CharField(max_length=20)
    emailid=models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('student-view')