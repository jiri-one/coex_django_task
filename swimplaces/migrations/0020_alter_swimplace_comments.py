# Generated by Django 4.1 on 2022-08-15 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0019_rename_comment_swimplace_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimplace',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='swimplaces.comment'),
        ),
    ]
