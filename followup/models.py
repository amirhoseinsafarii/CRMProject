from django.db import models
from . import enums
# Create your models here.

class FollowUP(models.Model):
    title = models.SlugField(max_length=50)
    organization = models.ForeignKey('organization.Organization', verbose_name='یرای سازمان', on_delete=models.PROTECT)
    created_on = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت گزارش')
    content = models.TextField(max_length=500, verbose_name='متن گزارش کار')
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)

    class Meta:
        permissions = []
        verbose_name = 'پیگیری'
        verbose_name_plural =' پیگیری ها'

class EmailHistory(models.Model):
    receiver = models.ForeignKey('organization.Organization', verbose_name='ارسال به',on_delete=models.PROTECT)
    status = models.CharField(max_length=10,verbose_name='وضعیت ارسال',choices=enums.EmailStatus.choices)
    send_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    sender = models.ForeignKey('auth.User', verbose_name='کاربر ارسال کننده', on_delete=models.PROTECT)

    class Meta:
        permissions = []
        verbose_name = 'تاریخجه ارسال ایمیل'
        verbose_name_plural ='تاریخچه ارسال ایمیل ها'

    