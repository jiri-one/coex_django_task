# Generated by Django 4.1 on 2022-08-15 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0018_comment_swimplace_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swimplace',
            old_name='comment',
            new_name='comments',
        ),
    ]
