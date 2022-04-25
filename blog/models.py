from django.db import models
from jalali_date import datetime2jalali, date2jalali
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='نویسنده')
    title = models.CharField(max_length=255, verbose_name='موضوع')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', verbose_name='تصویر')
    category = models.ManyToManyField(Category, blank=True, verbose_name='دسته بندی')
    # tag = 
    counted_views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    published_date = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ انتشار')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')

    class Meta:
        ordering = ('-published_date',)
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


    def __str__(self):
        return self.title

    def jalali_date(self):
        return date2jalali(self.published_date)
