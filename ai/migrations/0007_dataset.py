# Generated by Django 4.1.2 on 2023-04-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0006_alter_contour_ai_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.FileField(upload_to='zip/')),
            ],
        ),
    ]
