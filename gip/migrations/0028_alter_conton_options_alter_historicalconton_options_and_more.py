# Generated by Django 4.1.2 on 2023-02-23 08:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0027_historicalregion_name_en_historicalregion_name_ky_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conton',
            options={'verbose_name': 'Canton', 'verbose_name_plural': 'Canton'},
        ),
        migrations.AlterModelOptions(
            name='historicalconton',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Canton', 'verbose_name_plural': 'historical Canton'},
        ),
        migrations.AlterModelOptions(
            name='historicalsoilclass',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Soil type', 'verbose_name_plural': 'historical Soil types'},
        ),
        migrations.AlterModelOptions(
            name='historicalsoilclassmap',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical The polygon of soil type', 'verbose_name_plural': 'historical Polygons of soil type'},
        ),
        migrations.AlterModelOptions(
            name='historicalsoilfertility',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Soil fertility', 'verbose_name_plural': "historical Soils' fertility"},
        ),
        migrations.AlterModelOptions(
            name='historicalsoilproductivity',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Soil productivity', 'verbose_name_plural': "historical Soils' productivity"},
        ),
        migrations.AlterModelOptions(
            name='historicalvillage',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Village', 'verbose_name_plural': 'historical Villages'},
        ),
        migrations.AlterModelOptions(
            name='soilclass',
            options={'verbose_name': 'Soil type', 'verbose_name_plural': 'Soil types'},
        ),
        migrations.AlterModelOptions(
            name='soilclassmap',
            options={'verbose_name': 'The polygon of soil type', 'verbose_name_plural': 'Polygons of soil type'},
        ),
        migrations.AlterModelOptions(
            name='soilfertility',
            options={'verbose_name': 'Soil fertility', 'verbose_name_plural': "Soils' fertility"},
        ),
        migrations.AlterModelOptions(
            name='soilproductivity',
            options={'verbose_name': 'Soil productivity', 'verbose_name_plural': "Soils' productivity"},
        ),
        migrations.AlterModelOptions(
            name='village',
            options={'verbose_name': 'Village', 'verbose_name_plural': 'Villages'},
        ),
        migrations.AddField(
            model_name='historicalconton',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AddField(
            model_name='historicalconton',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AddField(
            model_name='historicalconton',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AddField(
            model_name='historicalculture',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Culture'),
        ),
        migrations.AddField(
            model_name='historicalculture',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Culture'),
        ),
        migrations.AddField(
            model_name='historicalculture',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Culture'),
        ),
        migrations.AddField(
            model_name='historicaldistrict',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='District'),
        ),
        migrations.AddField(
            model_name='historicaldistrict',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='District'),
        ),
        migrations.AddField(
            model_name='historicaldistrict',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='District'),
        ),
        migrations.AddField(
            model_name='historicalfertility',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Fertilizer'),
        ),
        migrations.AddField(
            model_name='historicalfertility',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Fertilizer'),
        ),
        migrations.AddField(
            model_name='historicalfertility',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Fertilizer'),
        ),
        migrations.AddField(
            model_name='historicalorthophoto',
            name='layer_name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Layer name'),
        ),
        migrations.AddField(
            model_name='historicalorthophoto',
            name='layer_name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Layer name'),
        ),
        migrations.AddField(
            model_name='historicalorthophoto',
            name='layer_name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Layer name'),
        ),
        migrations.AddField(
            model_name='historicalsoilclass',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='historicalsoilclass',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='historicalsoilclass',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='historicalsoilproductivity',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='historicalsoilproductivity',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='historicalsoilproductivity',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='historicalvillage',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='historicalvillage',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='historicalvillage',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='soilclass',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='soilclass',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='soilclass',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Soil type'),
        ),
        migrations.AddField(
            model_name='soilproductivity',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='soilproductivity',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='soilproductivity',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Soil productivity'),
        ),
        migrations.AddField(
            model_name='village',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='village',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='village',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Village'),
        ),
        migrations.AlterField(
            model_name='conton',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='conton',
            name='name_en',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='conton',
            name='name_ky',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='conton',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='contour',
            name='conton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contours', to='gip.conton', verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='historicalconton',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='historicalcontour',
            name='conton',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gip.conton', verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='historicalregion',
            name='density',
            field=models.FloatField(verbose_name='Density'),
        ),
        migrations.AlterField(
            model_name='historicalsoilclass',
            name='fertility',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gip.fertility', verbose_name='Fertilizer'),
        ),
        migrations.AlterField(
            model_name='historicalsoilclass',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Soil type'),
        ),
        migrations.AlterField(
            model_name='historicalsoilclassmap',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='historicalsoilclassmap',
            name='soil_class',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gip.soilclass', verbose_name='Soil type'),
        ),
        migrations.AlterField(
            model_name='historicalsoilfertility',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='historicalsoilfertility',
            name='soil_productivity',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gip.soilproductivity', verbose_name='Soil productivity'),
        ),
        migrations.AlterField(
            model_name='historicalsoilproductivity',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Soil productivity'),
        ),
        migrations.AlterField(
            model_name='historicalvillage',
            name='conton',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gip.conton', verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='historicalvillage',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Village'),
        ),
        migrations.AlterField(
            model_name='historicalvillage',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='region',
            name='density',
            field=models.FloatField(verbose_name='Density'),
        ),
        migrations.AlterField(
            model_name='soilclass',
            name='fertility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil_classes', to='gip.fertility', verbose_name='Fertilizer'),
        ),
        migrations.AlterField(
            model_name='soilclass',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Soil type'),
        ),
        migrations.AlterField(
            model_name='soilclassmap',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='soilclassmap',
            name='soil_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil_class_maps', to='gip.soilclass', verbose_name='Soil type'),
        ),
        migrations.AlterField(
            model_name='soilfertility',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='soilfertility',
            name='soil_productivity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil_fertility', to='gip.soilproductivity', verbose_name='Soil productivity'),
        ),
        migrations.AlterField(
            model_name='soilproductivity',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Soil productivity'),
        ),
        migrations.AlterField(
            model_name='village',
            name='conton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='gip.conton', verbose_name='Canton'),
        ),
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Village'),
        ),
        migrations.AlterField(
            model_name='village',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(geography='Kyrgyzstan', srid=4326, verbose_name='Polygon'),
        ),
    ]
