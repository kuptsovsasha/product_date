# Generated by Django 4.0 on 2021-12-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
