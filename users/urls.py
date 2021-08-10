from django.urls import path
from users.views import home
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path("home/",home,name="user-home"),
    path("login/",LoginView.as_view(template_name="users/Login.html"),name="login"),
    path("logout/",LogoutView.as_view(template_name="users/logout.html"),name="logout")

]