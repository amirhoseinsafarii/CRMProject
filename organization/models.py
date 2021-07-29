from django.db import models
from django.core.validators import RegexValidator
from django.db.models.deletion import PROTECT
from products.models import Product
# Create your models here.

phone_regex = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message='phone number invalid')

class Organization(models.Model):
    city = models.CharField(max_length=50, verbose_name='نام استان')
    organization_name = models.CharField(max_length=50, verbose_name='نام سازمان')
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    number_of_labor = models.IntegerField(verbose_name='تعداد کارگران')
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    Manufactured_products = models.ManyToManyField('products.OrganizationProducts', verbose_name='محصول تولیدی', blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=11, verbose_name='شماره تلفن')
    email = models.CharField(max_length=100 ,verbose_name='ایمیل')
    created_on = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.organization_name}'

    class Meta:
        permissions = []
        verbose_name = 'سازمان '
        verbose_name_plural = 'سازمان ها'


    def s_products(self):
        products = []

        for product in self.Manufactured_products.all():
            products += product.products_s()
        y = "".join(products)
        return y


    def org_product(self):
        for product in self.Manufactured_products.all():
            print(product.name)
        x = "".join(product.name)
        return x

