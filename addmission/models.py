from django.db import models
from student.models import student
from course.models import course
from django.urls import reverse
# Create your models here.
class addmission(models.Model):
    date=models.DateField()
    student=models.ForeignKey(student,on_delete=models.CASCADE,related_name='addmission')
    course=models.ForeignKey(course,on_delete=models.CASCADE,related_name='course')
    starttime=models.TimeField()
    endtime=models.TimeField()
    startdate=models.DateField()
    enddate=models.DateField()
    Fees=models.IntegerField()
    no_of_days=models.IntegerField()
    remarks=models.TextField(blank=True,null=True)
    pending_fees=models.IntegerField()


    def __str__(self):
        return f"{self.id}-{self.student.first_name}-{self.course.name}"

    def get_absolute_url(self):
        return reverse('addmission-view')