# Generated by Django 4.0 on 2022-01-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_item_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]