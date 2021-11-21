from typing import ClassVar
from django.contrib import admin

from .models import Psychologist, Patient


class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0


class PsychologistAdmin(admin.ModelAdmin):
    inlines = [PatientInline]
    

admin.site.register(Psychologist, PsychologistAdmin)

