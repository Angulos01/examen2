from django.contrib import admin
from api import models
# Register your models here.

@admin.register(models.Pendientes)
class Pendientes(admin.ModelAdmin):
    list_display = ["title", "description", "user", "timestamp", "priority", "state","status"]