# Generated by Django 4.1 on 2022-08-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0011_alter_swimplace_diving_alter_swimplace_entrance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimplace',
            name='nudist_beach',
            field=models.CharField(blank=True, choices=[('Suitable for nudists', 'Suitable for nudists'), ('Not suitable for nudists', 'Not suitable for nudists')], max_length=30, null=True),
        ),
    ]