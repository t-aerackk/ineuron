from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Appointment)
# admin.site.register(ImageHandler)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('tid', 'patient_name', 'appointment_date')
    readonly_fields = ('tid',)