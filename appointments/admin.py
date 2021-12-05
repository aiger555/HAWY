from django.contrib import admin

from .models import Appointment, PastAppointment


admin.site.register(Appointment)
admin.site.register(PastAppointment)
