# Generated by Django 5.0 on 2024-01-15 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_appointment_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='desc',
            new_name='des',
        ),
    ]
