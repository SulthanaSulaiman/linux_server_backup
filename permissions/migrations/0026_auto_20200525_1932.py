# Generated by Django 3.0.4 on 2020-05-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0025_auto_20200524_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='unit',
            name='chapter_title',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
