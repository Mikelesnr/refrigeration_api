from django.db import models
from technicians.models import Technician
from inventory.models import Unit

class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    technician = models.ForeignKey(Technician, related_name='jobs', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    used_stock = models.ManyToManyField(Unit, related_name='jobs', blank=True)
    payment_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
