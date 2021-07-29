from django.db import models
from django.utils.text import slugify
# Create your models here.

class FollowUP(models.Model):
    title = models.SlugField(max_length=50)
    content = models.TextField(max_length=500, verbose_name='متن گزارش کار')
    organization = models.ForeignKey('organization.Organization', verbose_name='یرای سازمان', on_delete=models.PROTECT)
    created_on = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت گزارش')
    user = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)

    class Meta:
        permissions = []
        verbose_name = 'پیگیری'
        verbose_name_plural =' پیگیری ها'

