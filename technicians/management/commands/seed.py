from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from technicians.models import Technician
from jobs.models import Job
from inventory.models import StockItem, Unit
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = "Seeds the database with initial data for all apps: technicians, jobs, and inventory."

    def handle(self, *args, **options):
        self.stdout.write("Clearing old data...")
        self.clear_data()

        self.stdout.write("Seeding new data...")
        technician = self.seed_superuser_and_technicians()
        if technician:
            self.seed_inventory()
            self.seed_jobs(technician)

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))

    def clear_data(self):
        """Clears data from all models before seeding."""
        Technician.objects.all().delete()
        Job.objects.all().delete()
        Unit.objects.all().delete()
        StockItem.objects.all().delete()

    def seed_superuser_and_technicians(self):
        """Seeds the superuser as a technician."""
        try:
            # Find the first superuser in the database
            superuser = User.objects.filter(is_superuser=True).first()
            if not superuser:
                self.stdout.write(self.style.ERROR("No superuser found. Please create a superuser first."))
                return None

            # Create a Technician linked to the superuser
            technician = Technician.objects.create(user=superuser, clocked_in=True)
            self.stdout.write(f"Technician added for superuser: {technician.user.username}")
            return technician
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error adding superuser as technician: {e}"))
            return None

    def seed_inventory(self):
        """Seeds inventory with stock items and units."""
        # Create stock items
        stock1 = StockItem.objects.create(name="Compressor", description="Refrigeration compressor")
        stock2 = StockItem.objects.create(name="Condenser", description="Refrigeration condenser")

        # Create units linked to stock items
        unit1 = Unit.objects.create(stock_item=stock1, quantity=10)
        unit2 = Unit.objects.create(stock_item=stock2, quantity=5)

        self.stdout.write(f"Inventory added: {stock1.name}, {stock2.name}")

    def seed_jobs(self, technician):
        """Seeds jobs and associates them with the given technician and inventory."""
        # Fetch inventory items
        unit1 = Unit.objects.first()
        unit2 = Unit.objects.last()

        # Verify that inventory exists
        if not unit1 or not unit2:
            self.stdout.write(self.style.ERROR("No inventory available. Jobs cannot be seeded."))
            return

        # Use make_aware to make datetime objects timezone-aware
        job1 = Job.objects.create(
            technician=technician,
            description="Repair condenser in supermarket",
            status="completed",
            start_time=make_aware(datetime(2025, 3, 1, 10, 0)),
            end_time=make_aware(datetime(2025, 3, 1, 15, 0)),
            payment_received=150.00
        )
        job1.used_stock.add(unit2)

        job2 = Job.objects.create(
            technician=technician,
            description="Replace compressor in cold room",
            status="pending",
            start_time=make_aware(datetime(2025, 3, 2, 8, 0)),
            end_time=make_aware(datetime(2025, 3, 2, 12, 0)),
            payment_received=0.00
        )
        job2.used_stock.add(unit1)

        self.stdout.write(f"Jobs added: {job1.description}, {job2.description}")
