import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refrigeration_api.settings')
django.setup()

from technicians.models import Technician
from jobs.models import Job
from inventory.models import StockItem, Unit
from django.contrib.auth.models import User
from datetime import datetime

def seed_data():
    # Clear existing data (be cautious in production)
    print("Clearing existing data...")
    Technician.objects.all().delete()
    Job.objects.all().delete()
    StockItem.objects.all().delete()
    Unit.objects.all().delete()

    # Seed StockItems and Units
    print("Seeding inventory...")
    compressor = StockItem.objects.create(name="Compressor", description="Refrigeration compressor")
    condenser = StockItem.objects.create(name="Condenser", description="Refrigeration condenser")
    unit1 = Unit.objects.create(stock_item=compressor, quantity=10)
    unit2 = Unit.objects.create(stock_item=condenser, quantity=5)

    # Seed Users and Technicians
    print("Seeding technicians...")
    user1 = User.objects.create_user(username="tech1", password="password123")
    user2 = User.objects.create_user(username="tech2", password="password123")
    tech1 = Technician.objects.create(user=user1, clocked_in=True)
    tech2 = Technician.objects.create(user=user2, clocked_in=False)

    # Assign personal inventory to technicians
    tech1.personal_inventory.add(unit1)
    tech2.personal_inventory.add(unit2)

    # Seed Jobs
    print("Seeding jobs...")
    job1 = Job.objects.create(
        technician=tech1,
        description="Repair condenser in supermarket",
        status="completed",
        start_time=datetime(2025, 3, 1, 10, 0),
        end_time=datetime(2025, 3, 1, 15, 0),
        payment_received=150.00
    )
    job1.used_stock.add(unit2)

    job2 = Job.objects.create(
        technician=tech2,
        description="Replace compressor in cold room",
        status="pending",
        start_time=datetime(2025, 3, 2, 8, 0),
        end_time=datetime(2025, 3, 2, 12, 0),
        payment_received=0.00
    )
    job2.used_stock.add(unit1)

    print("Seeding complete!")

if __name__ == '__main__':
    seed_data()
