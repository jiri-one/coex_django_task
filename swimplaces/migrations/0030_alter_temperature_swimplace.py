# Generated by Django 4.1 on 2022-08-20 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0029_alter_temperature_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='swimplace',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temperature', to='swimplaces.swimplace'),
        ),
    ]
