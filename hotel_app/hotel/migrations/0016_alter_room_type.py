# Generated by Django 4.2 on 2023-05-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_alter_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Superior', 'Superior'), ('Deluxe', 'Deluxe')], max_length=15),
        ),
    ]
