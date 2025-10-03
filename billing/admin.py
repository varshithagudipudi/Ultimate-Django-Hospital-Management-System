from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment', 'amount', 'paid', 'issued_date')
    list_filter = ('paid', 'issued_date')
    search_fields = ('patient__user__username',)
