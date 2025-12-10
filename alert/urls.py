"""
User account management.
"""
from django.urls import path
from alert.views import (HomeView,
                         SignUpView,
                         AlertView)
from django.contrib.auth.views import (LoginView,
                                       LogoutView)


app_name = "alert"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),

    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="alert:login"), name="logout"),
    path("alert/", AlertView.as_view(), name="alert"),
]
