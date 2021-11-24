from django.db import models

from accounts.models import Doctor


class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Star of rating'
        verbose_name_plural = 'Stars of rating'
        ordering = ['-value']


class Rating(models.Model):
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='doctor')

    def __str__(self):
        return f'{self.star} --- {self.doctor}'