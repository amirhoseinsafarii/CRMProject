# Generated by Django 3.2.5 on 2021-08-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0015_auto_20210811_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='name',
        ),
    ]
