# Generated by Django 3.2.5 on 2021-07-28 18:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='نام استان')),
                ('organization_name', models.CharField(max_length=50, verbose_name='نام سازمان')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن')),
                ('number_of_labor', models.IntegerField(verbose_name='تعداد کارگران')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='phone number invalid', regex='^0[0-9]{2,}[0-9]{7,}$')], verbose_name='شماره تلفن')),
                ('email', models.CharField(max_length=100, verbose_name='ایمیل')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('Manufactured_products', models.ManyToManyField(blank=True, to='products.OrganizationProducts', verbose_name='محصول تولیدی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سازمان ',
                'verbose_name_plural': 'سازمان ها',
                'permissions': [],
            },
        ),
    ]
