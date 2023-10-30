from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.LoginPage, name="login"),
    path("register/", views.RegisterPage, name="register"),
    path("add-member/",views.add_member, name="add_member"),
    path("logout/", views.LogoutPage, name="logout"),
]