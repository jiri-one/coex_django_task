# Generated by Django 4.1 on 2022-08-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0010_alter_swimplace_import_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimplace',
            name='diving',
            field=models.CharField(blank=True, choices=[('Suitable for diving', 'Suitable for diving'), ('Not suitable for diving', 'Not suitable for diving')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='swimplace',
            name='entrance',
            field=models.CharField(blank=True, choices=[('Entrance fee', 'Entrance fee'), ('No entrance fee', 'No entrance fee')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='swimplace',
            name='refreshment',
            field=models.CharField(blank=True, choices=[('Restaurant on site', 'Restaurant on site'), ('No restaurant', 'No restaurant')], max_length=50, null=True),
        ),
    ]