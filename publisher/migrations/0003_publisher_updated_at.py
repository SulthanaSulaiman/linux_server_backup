# Generated by Django 3.0.4 on 2020-05-16 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0002_remove_publisher_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
