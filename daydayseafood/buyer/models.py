from django.db import models

from seller.models import LoginUser, Goods, GoodsType


# Create your models here.
##############################
# 购物车模型
##############################
class Cart(models.Model):
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE)
    goods_number = models.IntegerField(verbose_name="商品的数量")
    # goods_total = models.FloatField(verbose_name="商品的小计")
    cart_user = models.ForeignKey(to=LoginUser, on_delete=models.CASCADE, verbose_name="买家")

    class Meta:
        db_table = "cart"


ORDER_STATUS = (
    (1, "未支付"),
    (2, "已支付"),
    (3, "待发货"),
    (4, "已发货"),
    (5, "拒收"),
    (6, "已完成"),
)


##############################
# 订单模型
##############################
class PayOrder(models.Model):
    order_number = models.CharField(max_length=36, unique=True, verbose_name="订单号")
    order_date = models.DateField(auto_now=True, verbose_name="订单创建时间")
    order_status = models.IntegerField(choices=ORDER_STATUS, verbose_name="订单状态")
    order_address = models.CharField(max_length=1024, verbose_name="送货地址")
    order_user = models.ForeignKey(to=LoginUser, on_delete=models.CASCADE, verbose_name="买家")

    class Meta:
        db_table = "pay_order"


##############################
# 订单商品模型
##############################
class OrderInfo(models.Model):
    order = models.ForeignKey(to=PayOrder, on_delete=models.CASCADE)
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE)
    goods_price = models.FloatField(verbose_name="商品的单价")
    # store = models.ForeignKey(to=LoginUser, on_delete=models.CASCADE, verbose_name="卖家")
    goods_count = models.IntegerField(verbose_name="购买的单品的数量")
    goods_total_price = models.FloatField(verbose_name="购买的单品的总金额")

    class Meta:
        db_table = "order_info"
