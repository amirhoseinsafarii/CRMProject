# Generated by Django 3.2.5 on 2021-08-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0003_alter_emailhistory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhistory',
            name='status',
            field=models.CharField(choices=[('SENT', 'Sent'), ('FAILED', 'Failed')], default='FAILED', max_length=20, verbose_name='وضعیت ارسال'),
        ),
    ]
