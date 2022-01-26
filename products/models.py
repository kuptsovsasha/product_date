from django.db import models
import datetime
# Create your models here.


class Shop(models.Model):

    name = models.CharField("Магазин", max_length=255, blank=True, null=True)
    number = models.IntegerField(primary_key=True, blank=False, null=False, default=1)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=False, null=False)


    def __str__(self):
        return f"{self.name}"



class Item(models.Model):
    name = models.CharField("Найменування", max_length=255, blank=True, null=True)
    shop = models.ForeignKey(Shop, max_length=255, blank=True, null=True, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, blank=True, null=True)
    CO_code = models.IntegerField(blank=True, null=False, default=1000)
    barcode = models.BigIntegerField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True, primary_key=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name