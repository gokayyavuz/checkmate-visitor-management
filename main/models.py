from django.db import models
from datetime import date
# Create your models here.

class Besucher(models.Model):
    STANDORTE = [
        ("München", "München"),
        ("Berlin", "Berlin"),
        ("Hamburg", "Hamburg"),
        ("Stuttgart", "Stuttgart")
    ]

    vorname = models.CharField(max_length=200, blank=False, null=False)
    nachname = models.CharField(max_length=200, blank=False, null=False)
    telefon = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    standort = models.CharField(choices=STANDORTE, max_length=50, blank=False, null=False)
    besuchstag = models.DateField(default=date.today, blank=False, null=False)
    besuchsgrund = models.TextField(blank=False, null=False)
    weitere_informationen = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vorname} {self.nachname} - {self.standort}"
    

