from django.db import models

PET_TYPES = (
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Dragon', 'Dragon')
)


def save(self, *args, **kwargs):
    if self.pet_type not in [x[0] for x in self.PET_TYPES]:
        raise ValueError('Invalid pet type')
    super(Pet, self).save(*args, **kwargs)
    

class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    hunger = models.IntegerField()
    energy = models.IntegerField()


# Fixed options for state only those that

    def __str__(self):
        return self.name


"""Example instance of a new pet
new_pet = Pet(pet_type="Dog", state="Idle", name="Rex", hunger=5, energy=8)
new_pet.save()
"""
