# Generated by Django 3.2.5 on 2021-08-11 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_alter_quote_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='name',
        ),
    ]