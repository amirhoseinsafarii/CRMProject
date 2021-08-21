from django.db import models
from django.core.validators import RegexValidator
from django.db.models.deletion import PROTECT
from products.models import Product
from django.utils.translation import ugettext_lazy as _
# Create your models here.

phone_regex = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message='phone number invalid')

class Organization(models.Model):
    """
        organization model
    """
    city = models.CharField(max_length=50, verbose_name=_('نام استان'))
    organization_name = models.CharField(max_length=50, verbose_name=_('نام سازمان'))
    phone = models.CharField(max_length=11, verbose_name=_('تلفن'))
    number_of_labor = models.IntegerField(verbose_name=_('تعداد کارگران'))
    full_name = models.CharField(max_length=50, verbose_name=_('نام و نام خانوادگی'))
    Manufactured_products = models.ManyToManyField('products.OrganizationProducts', verbose_name=_('محصول تولیدی'), blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=11, verbose_name=_('شماره تلفن'))
    email = models.CharField(max_length=100 ,verbose_name=_('ایمیل'))
    created_on = models.DateTimeField(verbose_name=_('تاریخ ایجاد'), auto_now_add=True)
    user = models.ForeignKey('auth.User', verbose_name=_('کاربر'), on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.organization_name}'

    class Meta:
        permissions = []
        verbose_name = 'سازمان '
        verbose_name_plural = 'سازمان ها'


    def suggestion_products(self):
        """
            list of suggestion products for organization
        """
        products = []

        for product in self.Manufactured_products.all():
            products += product.products_suggestion()
        return products


    def organization_products(self):
        """
            list of organization products
        """
        return [product.name for product in self.Manufactured_products.all()]


