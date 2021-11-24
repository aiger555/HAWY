from django.db import models

from accounts.models import User


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SpecifiedAssignment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.IntegerField()

    def __str__(self):
        return self.patient.username


class Choice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=240)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.question