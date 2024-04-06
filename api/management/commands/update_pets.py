from django.core.management.base import BaseCommand
from api.models import Pet

"""
*/30 * * * * /path/to/your/virtualenv/bin/python /path/to/your/manage.py update_pets

"""


class Command(BaseCommand):
    help = 'Increases the hunger and decreases the energy of all pets'

    def handle(self, *args, **kwargs):
        for pet in Pet.objects.all():
            pet.hunger = pet.hunger - 10  # Assuming 100 is max hunger
            pet.energy = pet.energy + 10
            pet.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated pets.'))
