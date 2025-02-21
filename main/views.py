from django.shortcuts import render, redirect, get_object_or_404
from .models import Besucher
from django.http import HttpResponse
from .forms import RegisterVisitor

# Create your views here.

def formular(request):
    if request.method == 'POST':
        form = RegisterVisitor(request.POST)
        print("Empfangene POST-Daten:", request.POST)  # Debugging
        
        if form.is_valid():
            besucher = form.save()
            print("Besucher gespeichert:", besucher)
            return redirect("finishView", besucher.id)
        else:
            print("Formular ist ungültig:", form.errors)  # Debugging

    else:
        form = RegisterVisitor()

    return render(request, 'main/formular.html', {'form': form})



def finishView(request, besucher_id):
    besucher = get_object_or_404(Besucher, id=besucher_id)
    return render(request, "main/finishView.html", {"besucher": besucher})

def aboutus(request):
    return render(request, "main/aboutus.html")

def terms(request):
    return render(request, "main/terms.html")

def home(request):
    return render(request, "main/home.html")

def contact(request):
    return render(request, "main/contact.html")