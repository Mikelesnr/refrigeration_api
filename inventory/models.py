from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Unit(models.Model):
    stock_item = models.ForeignKey(StockItem, related_name='units', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
