# Generated by Django 3.0.4 on 2020-04-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0008_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='requested_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
