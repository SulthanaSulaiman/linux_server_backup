# Generated by Django 3.0.4 on 2020-05-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0034_contact_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]