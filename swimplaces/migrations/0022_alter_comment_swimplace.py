# Generated by Django 4.1 on 2022-08-15 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swimplaces', '0021_remove_swimplace_comments_comment_swimplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='swimplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='swimplaces.swimplace'),
        ),
    ]
