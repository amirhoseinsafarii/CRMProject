from django.db import models
# Create your models here.

class Quote(models.Model):
    
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)
    create_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    organization = models.ForeignKey('organization.Organization', verbose_name='سازمان', on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.organization.organization_name}'

    class Meta:
        permissions = []
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتورها'

        unique_together = ['organization']

    
class QuoteItem(models.Model):
    
    quote = models.ForeignKey('quote.Quote', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', verbose_name='کالا', on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    discount = models.PositiveIntegerField(default=0, verbose_name='تخفیف')
    pricee = models.IntegerField(verbose_name='قیمت', default=0)

    def __str__(self):
        return f'{self.quote}'

    def price(self):
        t = 0
        d = 0
        if self.product.is_Includesـtaxes:
            t = (self.qty * self.product.price) * (9 / 100)
            t = (self.qty * self.product.price) + t
            d = t * (self.discount/100)
            t = t - d
            return t
            
    def save(self, *args, **kwargs):
        self.pricee = self.price()
        super(QuoteItem, self).save()

    class Meta:
        permissions = []
        verbose_name = ' ایتم پیش فاکتور'
        verbose_name_plural = 'ایتم های پیش فاکتور'

        unique_together = ['product', 'quote']

