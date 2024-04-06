from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    hunger = models.IntegerField()
    energy = models.IntegerField()



"""Example instance of a new pet
new_pet = Pet(pet_type="Dog", state="Idle", name="Rex", hunger=5, energy=8)
new_pet.save()
"""
