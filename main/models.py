from django.db import models
from datetime import date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils.text import slugify

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


class CompanyManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Die E-Mail-Adresse ist erforderlich")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Company(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CompanyManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name