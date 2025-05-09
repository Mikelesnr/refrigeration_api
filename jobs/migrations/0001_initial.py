# Generated by Django 5.1.7 on 2025-03-14 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('technicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('payment_received', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='technicians.technician')),
                ('used_stock', models.ManyToManyField(blank=True, related_name='jobs', to='inventory.unit')),
            ],
        ),
    ]
