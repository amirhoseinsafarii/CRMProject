# Generated by Django 3.2.5 on 2021-08-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0008_alter_quote_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='نام سازمان'),
        ),
    ]
