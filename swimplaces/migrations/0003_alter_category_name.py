# Generated by Django 4.1 on 2022-08-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='No category', max_length=100, unique=True),
        ),
    ]
