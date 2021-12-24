from django.utils.translation import gettext_lazy as _
from django.db import models

from accounts.models import Doctor, Patient



class Appointment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    pats = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    docs = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    services = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f'StartTime={self.start_time} | EndTime={self.end_time} | Doctor={self.docs} | Patient={self.pats}'

    class Meta:
        ordering = ['start_time']


