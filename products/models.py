from django.db import models

# Create your models here.


class Item(models.Model):

    name = models.CharField("Найменування", max_length=255, blank=True, null=True)
    shop = models.CharField("Магазин", max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    CO_code = models.IntegerField(primary_key=True, blank=True, null=False, default=1000)
    barcode = models.BigIntegerField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.name