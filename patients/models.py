
# patients/models.py
from django.utils import timezone
from django.db import models
from core.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"