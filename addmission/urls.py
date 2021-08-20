from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewAddmissionView.as_view(),name="addmission-new"),
    path("view/",ListAddmissionView.as_view(),name="addmission-view"),
    path("update/<int:pk>",UpdateAddmissionView.as_view(),name="addmission-update"),
    path("delete/<int:pk>",DeleteAddmissionView.as_view(),name="addmission-delete"),
    path("detail/<int:pk>",DetailAddmission.as_view(),name="addmission-detail")
]