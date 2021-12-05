from django.core.validators import int_list_validator
from django.utils.translation import gettext_lazy as _
from django.db import models

from accounts.models import Doctor, Patient



class Appointment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    pats = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    docs = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    services = models.CharField(max_length=1000, validators=[int_list_validator], blank=False, null=False)

    def __str__(self):
        return f'StartTime={self.start_time} | EndTime={self.end_time} | Doctor={self.docs} | Patient={self.pats}'

    class Meta:
        ordering = ['start_time']


class PastAppointment(models.Model):
    created = models.DateTimeField(blank=False, null=False)
    appointment_id = models.IntegerField(blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    patient = models.ForeignKey(Patient, related_name='past_appointment_patient', on_delete=models.CASCADE, blank=False, null=True)
    doctor = models.ForeignKey(Doctor, related_name='past_appointment_doctor', on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return f'StartTime={self.start_time} | EndTime={self.end_time} | Doctor={self.doctor} | Patient={self.patient}'

    class Meta:
        ordering = ['start_time']