# Generated by Django 3.2.5 on 2021-08-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0009_quote_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='slug',
            field=models.SlugField(default=1, verbose_name='نام سازمان'),
            preserve_default=False,
        ),
    ]
