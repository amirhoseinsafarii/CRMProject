
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام محصول',db_index=True)
    price = models.PositiveIntegerField(default=0, db_index=True)
    is_Includesـtaxes = models.BooleanField(default=False,verbose_name='ایا مشمول مالیات است؟')
    image = models.ImageField(verbose_name='عکس محصول')
    description = models.TextField(verbose_name='توضحیات محصول',help_text='متن نمایشی برای توصیف محصول')

    def __str__(self):
        return f'{self.name}'


    

    class Meta:
        permissions = []
        verbose_name = 'محصول شرکت '
        verbose_name_plural = 'محصولات شزکت'


class OrganizationProducts(models.Model):
    name = models.CharField(max_length=100)
    s_products = models.ManyToManyField('products.Product')


    class Meta:
        permissions = []
        verbose_name = 'محصول تولیدی سازمان ها '
        verbose_name_plural = 'محصولات تولیدی سازمان ها'

    def __str__(self):
        return self.name

    def products_s(self):
        for product in self.s_products.all():
             print(product.name)
        x = "".join(product.name)
        return x
    

    def p(self):
        products = []

        for product in self.name.all():
            products += product.org_product()
        y = "".join(products)
        return y

    
    