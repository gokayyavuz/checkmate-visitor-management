from django import forms
from . import models

class RegisterVisitor(forms.ModelForm):
    class Meta:
        model = models.Besucher
        fields = ['vorname', 'nachname', 'telefon', 'email', 'standort', 'besuchstag', 'besuchsgrund', 'weitere_informationen']