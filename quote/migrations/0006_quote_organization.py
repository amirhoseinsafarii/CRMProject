# Generated by Django 3.2.5 on 2021-08-03 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('quote', '0005_remove_quoteitem_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='organization.organization', verbose_name='سازمان'),
            preserve_default=False,
        ),
    ]
