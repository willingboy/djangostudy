from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest


def alipayconfig():
    # 实例化阿里支付配置信息对象
    alipay_config = AlipayClientConfig(sandbox_debug=True)
    # 阿里提供的服务接口，这个是测试接口，真实支付接口：https://openapi.alipay.com/gateway.do
    alipay_config.server_url = "https://openapi.alipaydev.com/gateway.do"
    # 申请的沙箱环境的app_id
    alipay_config.app_id = "2016101800717513"
    # 商户的私钥
    alipay_config.app_private_key = "MIIEpAIBAAKCAQEAv1339WKBm7b6iR6Dl59AM15Z3+duCc4cG1EOyhs8DmmVmVo/AQNb/XdSjT3ocBXEwNjwNhu7HN9xHOo68+slB4ngTL9Q3K/0BbN2mbKP57JgtDJEBBWoF7PTfCMOHj70tIYFS6JQyh81G1aX7DnnAyhKqXzfhZn/UTyvNr9Y6OksHOIdteIHnJNT+QqdCXCbjViuUWFMbWw2YXEqGu5/qAyRa9W+VSveX+LqYhBtsJWQhmxPWpd72yo5jqIsQTcuwR2CinFPAnI9LKYfdYiwgBmVeaf/p6Gijgea+y+vQjkm9y7V8P2YP+Z1OQU0PkHtTWTUfskvtTX3mgpFvabABwIDAQABAoIBAQCHZNSqqKdKpItduFkiTWn+7iJoaDVSeqEoMpFkLSCwkcNmXJN3BAlxq5qck9CAfOZYCyTpI3WfV/ePnalYKmZojwRDSJjNiy/7WJ3w4IUwSORima3FtgzXuENI8QRsId7AWpIkkRLX7nyEex/B4rWvZjJs+AytWedqcqUE9xzQq+y7uj9FAbNntIGD8GPWH+Y/AAbRdpHK9vTLbQ+SQlypzZQ/03pvrychPPSRgPivP35bxOtVxAiDp9uxu2LwyLV6cSCeEPB2xlSyEYI8rYbyilWb7sFENwi+JAGV03lhpVaQcpWKmD9GgYTf3F88icchEN5iGh32v2yWyoFaQYABAoGBAPyOrOoJtdyEKRCKE9yT2iKpwc0zBVbbZfLe0P67dlCf2h2JCO2ZTctBQEYHDxQnP5HczYOZip3UXL0u1IkTlYaP4g2IaS2GZ47Z49GgfoPgS8iG9JeT178Z9a5u4ZfXsFSAnxCcSR62xOE7Dz/AzLLxBIXx/J9KFrOtMum4Sv4BAoGBAMH5w3Oh64w2wl9jvA2hNJ13bjZa+QELtEnbe3Lt8i7JxlbWY+cnaKMx3sRuJM4NLXYevJ1RfAEkZLjU/LHznkQAQdg279inBjNmgx6U/zNWY5MkJTMlrNetELBWIGz8eVFfA3V9cMEYaLb3PYNIDYAWR+3OCHTDpmb15pjFNc4HAoGBAPXNRq1hVgaQ+gaG3F3J6HvkDCLSjVfDoK2H/pBtkvFVIsusG2xj0DsJ/qwpIpvStyQXak2ymh6SGNBnS6M91EFqt+/D29na/d8iYYAcXAWtvxQjhNohodD0SxDCCf3mhk83/5gDA4dJCsTK3kSGOLPPrz9ODThau02UPAEMxLABAoGACbSEafGtBlvrB7jGvOvW5RYHpqKQmNPMFnHr0ElFd7/Ss5+Qag1Xt+qT2cIlB0YzgxhwmXJtQOVgQLsvVXv57C8THE1LXMymi8XSQ6Jyzk/BNah2UAPPjQ70qc31W16ad07IroUzMgYVnynpovrk6gazXJuVYrozRi2Bdx1O3tsCgYBHClQR6/fTjkZqD23kzlKYKi+zObZ1ijTlscjn7tQFMX0IFoFjbW5mbNBwTXGL/ujIsqdDx9NQyDOTllpb3uutpKy4zcWRGlZDWZaidZTLhbzp08A9W7N/sfJQ5cqwL/tEYVx3am+CxTgXd1tO6MsedK5Drde7MuBXN8Tr3Bof7g=="
    # 阿里的公钥
    alipay_config.alipay_public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv1339WKBm7b6iR6Dl59AM15Z3+duCc4cG1EOyhs8DmmVmVo/AQNb/XdSjT3ocBXEwNjwNhu7HN9xHOo68+slB4ngTL9Q3K/0BbN2mbKP57JgtDJEBBWoF7PTfCMOHj70tIYFS6JQyh81G1aX7DnnAyhKqXzfhZn/UTyvNr9Y6OksHOIdteIHnJNT+QqdCXCbjViuUWFMbWw2YXEqGu5/qAyRa9W+VSveX+LqYhBtsJWQhmxPWpd72yo5jqIsQTcuwR2CinFPAnI9LKYfdYiwgBmVeaf/p6Gijgea+y+vQjkm9y7V8P2YP+Z1OQU0PkHtTWTUfskvtTX3mgpFvabABwIDAQAB"

    # 实例化一个支付对象放回
    alipay_client = DefaultAlipayClient(alipay_client_config=alipay_config)
    return alipay_client


class Alipay(object):
    def __init__(self):
        # 得到阿里支付的实例化对象
        self.client = alipayconfig()
        # 为API生成一个模版对象，初始化参数用的
        self.model = AlipayTradePagePayModel()
        # 实例化一个请求对象
        self.request = AlipayTradePagePayRequest(biz_model=self.model)

    def payurl(self):
        # 利用阿里支付对象发送一个获得页面的请求，参数是request
        response = self.client.page_execute(self.request, http_method="GET")
        # 返回支付宝链接跳转
        return response

    def orders(self, data, user):
        import json
        from buyer.models import PayOrder
        total_money = 0
        payorder = PayOrder.objects.filter(order_number=data['order_number'], order_user=user).first()
        goods = payorder.orderinfo_set.all()
        for i in goods:
            money = i.goods_price * i.goods_count
            total_money += money
        total_money += 10  # 运费
        self.model.out_trade_no = payorder.order_number
        self.model.total_amount = total_money
        self.model.subject = user.username
        self.model.body = json.dumps(data['goods_list'])
        self.model.product_code = "FAST_INSTANT_TRADE_PAY"
        self.request.return_url = "http://117.67.47.105:80/buyer/alipay"
        self.request.notify_url = "http://117.67.47.105:80/buyer/alipay"
        return self.payurl()


if __name__ == "__main__":
    alipay = Alipay()
    # 订单号
    alipay.model.out_trade_no = "pay6514876546"
    # 金额
    alipay.model.total_amount = "88888.00"
    # 商品标题
    alipay.model.subject = "支付宝开发测试"
    # 商品的详细内容
    alipay.model.body = "支付宝测试"
    # 销售产品码，与支付宝签约的产品名称
    alipay.model.product_code = "FAST_INSTANT_TRADE_PAY"

    # get请求 用户支付成功后返回的页面请求地址
    alipay.request.return_url = "http://127.0.0.1:8000/alipay"
    # post请求 用户支付成功同志商户的请求地址
    alipay.request.notify_url = "http://127.0.0.1:8000/alipay"

    r = alipay.payurl()
    print("打印支付页面地址:\n", r)
