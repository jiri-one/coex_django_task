# Generated by Django 4.1 on 2022-08-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0015_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
