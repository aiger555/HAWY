from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    probem_title = models.CharField(max_length=200)
    problem_body = models.TextField()

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    probem_title = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    sertificate = models.ImageField(blank=False)
    experience_of_work = models.TextField()

    def __str__(self):
        return self.user.username
