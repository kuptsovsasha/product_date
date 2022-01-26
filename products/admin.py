from django.contrib import admin
from .models import Item, Shop
# Register your model


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'CO_code', 'department', 'shop')
    search_fields = ["CO_code"]
    ordering = ('name',)

class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = ('name', 'number', 'address')



admin.site.register(Shop)