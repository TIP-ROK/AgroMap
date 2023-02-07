# Generated by Django 4.1.2 on 2023-01-23 11:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0012_landtype_rename_sum_ha_contour_area_ha_and_more'),
        ('culture_model', '0003_rename_index_vegetationindex'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indexes', '0011_productivityclass_historicalproductivityclass_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexFact',
            new_name='ActuaVegIndex',
        ),
        migrations.RenameModel(
            old_name='HistoricalIndexFact',
            new_name='HistoricalActuaVegIndex',
        ),
    ]