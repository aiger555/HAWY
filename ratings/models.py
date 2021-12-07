from django.db import models

from accounts.models import Doctor


class Rating(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.SET_NULL, null=True)
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return f'{self.value} -- {self.doctor}'


