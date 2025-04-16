from django.db import models
from django.contrib.auth.models import User
from inventory.models import Unit

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clocked_in = models.BooleanField(default=False)
    personal_inventory = models.ManyToManyField(Unit, related_name='technicians', blank=True)
