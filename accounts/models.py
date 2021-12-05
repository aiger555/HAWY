from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
  is_doctor = models.BooleanField(default=False)
  is_patient = models.BooleanField(default=False)


class Doctor(models.Model):
    doctor = models.OneToOneField(
                                settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                blank=True, 
                                null=True
                                )
    age = models.PositiveIntegerField(blank=True)
    sertificate = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return self.doctor.username


class Patient(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.patient.username