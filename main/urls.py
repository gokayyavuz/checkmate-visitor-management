from django.urls import path
from . import views

urlpatterns = [
    path("", views.formular, name="formular"),
    path("finish/<int:besucher_id>/", views.finishView, name="finishView"), 
]
