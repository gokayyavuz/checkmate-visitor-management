from django.shortcuts import render
from .models import Besucher
from django.http import HttpResponse
from . import forms

# Create your views here.

def formular(response):
    form = forms.RegisterVisitor()
    return render(response, 'main/formular.html', {'form': form})


def finishView(response):
    besucher = Besucher.objects.get()
    return render(response, 'main/finishView.html', {"bs": besucher})