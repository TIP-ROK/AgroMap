# Generated by Django 4.1.2 on 2023-01-11 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexes', '0003_historicalindexfact_date_indexfact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalindexfact',
            name='source',
        ),
        migrations.RemoveField(
            model_name='indexfact',
            name='source',
        ),
    ]