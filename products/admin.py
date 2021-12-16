from django.contrib import admin
from .models import Item
# Register your model


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('CO_code', 'department', 'shop')


admin.site.register(Item)