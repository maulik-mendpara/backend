# Generated by Django 5.0 on 2024-01-11 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aouthapp', '0002_addsignup_delete_usersignup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addsignup',
            old_name='mobile',
            new_name='phon',
        ),
    ]
