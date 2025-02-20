from django import forms
from . import models

class RegisterVisitor(forms.ModelForm):
    class Meta:
        model = models.Besucher
        fields = ['vorname', 'nachname', 'telefon', 'email', 'standort', 'besuchstag', 'besuchsgrund', 'weitere_informationen']
        error_messages = {
            'vorname': {
                'required': "Bitte geben Sie Ihren Vornamen ein.",
                'max_length': "Der Name darf maximal 200 Zeichen lang sein."
            },
            'nachname': {
                'required': "Bitte geben Sie Ihren Nachnamen ein."
            },
            'telefon': {
                'required': "Bitte geben Sie eine gültige Telefonnummer ein."
            },
            'email': {
                'required': "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
                'invalid': "Bitte geben Sie eine gültige E-Mail-Adresse ein."
            },
            'standort': {
                'required': "Bitte wählen Sie einen Standort aus."
            },
            'besuchstag': {
                'required': "Bitte wählen Sie ein Besuchsdatum."
            },
            'besuchsgrund': {
                'required': "Bitte geben Sie den Grund Ihres Besuchs an."
            }
        }