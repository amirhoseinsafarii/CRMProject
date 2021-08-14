
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام محصول',db_index=True)
    price = models.PositiveIntegerField(default=0, db_index=True)
    is_Includesـtaxes = models.BooleanField(default=False,verbose_name='ایا مشمول مالیات است؟')
    image = models.ImageField(verbose_name='عکس محصول')
    pdf = models.FileField(upload_to='pdf', verbose_name='کاتالوگ', blank=True, null=True)
    description = models.TextField(verbose_name='توضحیات محصول',help_text='متن نمایشی برای توصیف محصول')

    def __str__(self):
        return self.name


    

    class Meta:
        permissions = []
        verbose_name = 'محصول شرکت '
        verbose_name_plural = 'محصولات شزکت'


class OrganizationProducts(models.Model):
    name = models.CharField(max_length=100)
    suggestion_products = models.ManyToManyField('products.Product')


    class Meta:
        permissions = []
        verbose_name = 'محصول تولیدی سازمان ها '
        verbose_name_plural = 'محصولات تولیدی سازمان ها'

    def __str__(self):
        return self.name

    def products_suggestion(self):
        return [product.name for product in self.suggestion_products.all()]

    def prudoct(self):
        return [self.name]
       
    

    def products(self):
        products = []

        for product in self.name.all():
            products += product.organization_products()
        y = "".join(products)
        return y

    
    