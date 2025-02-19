from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def formular(response):
    return render(response, 'main/formular.html')


def finishView(response):
    return render(response, 'main/finishView.html')