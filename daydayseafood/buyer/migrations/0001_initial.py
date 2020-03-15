# Generated by Django 3.0.4 on 2020-03-11 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0004_auto_20200311_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.IntegerField(verbose_name='商品的数量')),
                ('goods_total', models.FloatField(verbose_name='商品的小计')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.LoginUser', verbose_name='买家')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Goods')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
