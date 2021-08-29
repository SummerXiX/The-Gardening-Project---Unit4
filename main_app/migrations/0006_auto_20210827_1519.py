# Generated by Django 3.2.6 on 2021-08-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_cat_photo_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Plant Care Instructions'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='time',
            field=models.IntegerField(verbose_name='Years Since Planted/Bought'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Plant Type'),
        ),
    ]