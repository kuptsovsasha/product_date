# Generated by Django 4.0 on 2021-12-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Найменування')),
                ('shop', models.CharField(blank=True, max_length=255, null=True, verbose_name='Магазин')),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('CO_code', models.IntegerField(blank=True, default=1000, primary_key=True, serialize=False)),
                ('barcode', models.IntegerField(blank=True, null=True)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
    ]
