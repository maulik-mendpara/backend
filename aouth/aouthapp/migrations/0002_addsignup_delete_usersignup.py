# Generated by Django 5.0 on 2024-01-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aouthapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addsignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='usersignup',
        ),
    ]
