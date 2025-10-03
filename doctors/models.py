# doctors/models.py
from django.db import models
from core.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    availability = models.TextField()

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"

