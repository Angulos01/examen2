from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

CHOICES_PRIORITY = (
    ("ALTA", "ALT"),
    ("MEDIA", "MD"),
    ("BAJA", "BJ"),
)

CHIOCES_STATE = (
    ("SIN_RESOLVER", "Sin resolver"),
    ("PENDIENTE", "Pendiente"),
    ("RESUELTO", "Resuelto"),
)

class Pendientes(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    priority = models.CharField(max_length=8, choices=CHOICES_PRIORITY)
    state = models.CharField(max_length=16, choices=CHIOCES_STATE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
