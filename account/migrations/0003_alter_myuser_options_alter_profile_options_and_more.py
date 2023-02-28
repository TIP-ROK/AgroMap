# Generated by Django 4.1.2 on 2023-02-24 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_farmer',
            field=models.BooleanField(default=False, verbose_name='Farmer'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_supervisor',
            field=models.BooleanField(default=False, verbose_name='Supervisor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=55, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='my_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='My status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=14, verbose_name='Phone number'),
        ),
    ]