from django.db import models
from django.conf import settings


class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    hunger = models.IntegerField()
    energy = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)