# billing/models.py
from django.db import models
from patients.models import Patient
from appointments.models import Appointment

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill {self.id} - {self.patient.user.username} - {self.amount}"
