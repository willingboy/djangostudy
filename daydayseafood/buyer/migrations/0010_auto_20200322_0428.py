# Generated by Django 3.0.4 on 2020-03-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0009_auto_20200322_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='order_number',
            field=models.CharField(max_length=8, null=True, verbose_name='订单号'),
        ),
    ]