from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #path("company/<slug:slug>/", views.CompanyDetailView.as_view(), name="company_detail"),
    path("form/",views.formular, name="formular"),
    path("finish/<int:besucher_id>/", views.finishView, name="finishView"), 
    path("about-us/", views.aboutus, name="aboutus"),
    path("terms/", views.terms, name="terms"),
    path("contact/", views.contact, name="contact")
]
