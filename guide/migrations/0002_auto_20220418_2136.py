# Generated by Django 3.2.12 on 2022-04-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AlterField(
            model_name='paper',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
