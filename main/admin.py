from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Besucher, Company
# Register your models here.
admin.site.register(Besucher)

class CompanyAdmin(UserAdmin):
    model = Company
    list_display = ["email", "name", "industry", "website", "is_active", "is_staff"]
    list_filter = ["is_staff", "is_active"]
    ordering = ["email"]
    search_fields = ["email", "name"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Persönliche Informationen", {"fields": ("name", "industry", "website")}),
        ("Berechtigungen", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Wichtige Daten", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "industry", "website", "password1", "password2"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")

admin.site.register(Company, CompanyAdmin)