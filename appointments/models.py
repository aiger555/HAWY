from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from issues.models import Issue


class User(AbstractUser):
    is_psychologist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Psychologist(models.Model):
    psychologist = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='psychologists', blank=True, null=True)
    issue = models.ManyToManyField(Issue, related_name='issue')
    age = models.IntegerField()
    experience_of_work = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.psychologist.username

class Patient(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    psychologist = models.ForeignKey(Psychologist, on_delete=models.SET_NULL, null=True, related_name='doctor')
    name = models.CharField(max_length=250)
    registration_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name