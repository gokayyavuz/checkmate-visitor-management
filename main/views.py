from django.shortcuts import render, redirect
from .models import Besucher
from django.http import HttpResponse
from . import forms

# Create your views here.

def formular(response):
    if response.method == 'POST':
        form = forms.RegisterVisitor(response.POST)
        if form.is_valid():
            print('Versuch es zu speichern')
            form.save()
            print('wurde gespeichert')
            return redirect("finishView")
    else:
        form = forms.RegisterVisitor()
    return render(response, 'main/formular.html', {'form': form})


def finishView(response):
    besucher = Besucher.objects.get()
    return render(response, 'main/finishView.html', {"bs": besucher})