from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    # Use actual fields from your model
    list_display = ('first_name', 'last_name', 'age', 'gender', 'email', 'phone', 'created_at')

admin.site.register(Patient, PatientAdmin)
