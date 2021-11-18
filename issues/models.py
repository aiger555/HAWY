from django.db import models
from accounts.models import User


class Issue(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title

   

