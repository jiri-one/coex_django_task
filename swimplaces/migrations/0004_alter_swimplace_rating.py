# Generated by Django 4.1 on 2022-08-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimplace',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
