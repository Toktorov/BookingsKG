# Generated by Django 3.2.7 on 2021-09-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20210921_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='payment',
            field=models.CharField(choices=[('USD', 'USD'), ('EURO', 'EURO'), ('KGZ', 'KGZ'), ('RUB', 'RUB')], default='All payment', max_length=255, verbose_name='Оплата валюта:'),
        ),
    ]
