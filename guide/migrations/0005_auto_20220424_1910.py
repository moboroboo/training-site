# Generated by Django 3.2.12 on 2022-04-24 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0004_auto_20220419_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ('-created_date',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
        migrations.AlterField(
            model_name='paper',
            name='category',
            field=models.ManyToManyField(blank=True, to='guide.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='content',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='counted_views',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='image',
            field=models.ImageField(default='guide/default.jpg', upload_to='guide/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='published_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.BooleanField(default=False, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(max_length=255, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='translator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='مترجم'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی'),
        ),
    ]