# Generated by Django 5.0.1 on 2024-02-28 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_advertise'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertise',
            options={'verbose_name': 'Advertise', 'verbose_name_plural': 'Advertises'},
        ),
        migrations.AlterModelTable(
            name='advertise',
            table='advertise',
        ),
    ]