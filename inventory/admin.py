from django.contrib import admin
from .models import StockItem, Unit

# Register the StockItem and Unit models
admin.site.register(StockItem)
admin.site.register(Unit)
