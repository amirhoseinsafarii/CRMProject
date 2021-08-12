# Generated by Django 3.2.5 on 2021-08-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0014_remove_quote_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
