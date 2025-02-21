from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form/",views.formular, name="formular"),
    path("finish/<int:besucher_id>/", views.finishView, name="finishView"), 
    path("about-us/", views.aboutus, name="aboutus"),
    path("terms/", views.terms, name="terms"),
    path("contact/", views.contact, name="contact")
]
