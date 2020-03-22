from Qshop.models import *


class Goods(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goods_number = db.Column(db.String(11), unique=True)  # 商品编号
    goods_name = db.Column(db.String(32))  # 商品名字
    goods_price = db.Column(db.Float)  # 商品价格
    goods_count = db.Column(db.Integer)  # 商品数量
    goods_location = db.Column(db.String(32))  # 商品产地
    goods_safe_date = db.Column(db.Integer)  # 商品保质期
    goods_pro_time = db.Column(db.DateTime)  # 生成日期
    goods_status = db.Column(db.Boolean, default=1)  # 商品状态
    goods_picture = db.Column(db.String(32))  # "商品的图片"
    goods_description = db.Column(db.Text)  # 商品的描述
    goods_type = db.Column(db.Integer, db.ForeignKey("goods_type.id"))  # 商品类别
    goods_store = db.Column(db.Integer, db.ForeignKey("user.id"))  # 卖家

    def __str__(self):
        return self.goods_name


class GoodsType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_label = db.Column(db.String(32))
    type_description = db.Column(db.String(32))
    type_picture = db.Column(db.String(128))
    goods = db.relationship(Goods, backref="goodtype_set")

    def __str__(self):
        return self.type_label


db.create_all()
