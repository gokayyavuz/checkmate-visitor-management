from django.urls import path
from . import views

urlpatterns = [
    path("", views.formular, name="formular"),
    path("finish/", views.finishView, name="finishView"),
]