# Generated by Django 4.2 on 2023-05-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminworkenv', '0002_checkin_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]
