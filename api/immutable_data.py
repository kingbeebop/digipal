from pathlib import Path
import os
from models import Pet

# Bryan Mejia

# Created tupular array with stored Pet Types

PET_TYPES = (
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Dragon', 'Dragon')
)


# Designed function to store saved arguments into Object with Error Check
def _pet_type(*args, **kwargs):
    if self.pet_type not in [x[0] for x in self.PET_TYPES]:
        raise ValueError('Invalid pet type')
    super(Pet, self).save(*args, **kwargs)


#Tupular array with stored State Types
STATE_TYPES = (
    ('Idle', 'Idle'),
    ('Sleeping', 'Sleeping'),
    ('Eating', 'Eating'),
    ('Playing', 'Playing')
)


def save_state_type(self, *args, **kwargs):
    if self.state not in [x[0] for x in self.STATE_TYPES]:
        raise ValueError('Invalid State Type.')
    super(Pet, self).save(*args, **kwargs)
