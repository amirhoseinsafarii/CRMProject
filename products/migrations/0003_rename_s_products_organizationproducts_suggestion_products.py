# Generated by Django 3.2.5 on 2021-08-14 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizationproducts',
            old_name='s_products',
            new_name='suggestion_products',
        ),
    ]