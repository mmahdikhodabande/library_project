# Generated by Django 4.2.6 on 2023-10-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0005_alter_orderdetail_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد محصول'),
        ),
    ]