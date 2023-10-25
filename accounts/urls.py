from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.LoginPage, name="login"),
    path("register/", views.RegisterPage, name="register"),
    path("logout/", views.LogoutPage, name="logout"),
]