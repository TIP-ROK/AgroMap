# Generated by Django 4.1.2 on 2022-11-02 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0013_season_fieldinseason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soilanalysis',
            name='field',
        ),
        migrations.AddField(
            model_name='soilanalysis',
            name='field_polygon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='soil_analysis', to='plot.fieldpolygon'),
            preserve_default=False,
        ),
    ]
