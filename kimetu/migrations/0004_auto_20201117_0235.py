# Generated by Django 3.1.3 on 2020-11-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kimetu', '0003_auto_20201117_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('男', '女')], max_length=250, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('男', '女')], max_length=250, verbose_name='性別'),
        ),
    ]
