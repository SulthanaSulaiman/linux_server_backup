# Generated by Django 3.0.4 on 2020-05-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0023_auto_20200522_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='followedup_at',
            field=models.DateTimeField(null=True),
        ),
    ]
