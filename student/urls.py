from django.urls import path
from .views import *
urlpatterns=[
        path("new/",NewStudentView.as_view(),name="student-new"),
        path("view/",ViewStudent.as_view(),name="student-view")
]