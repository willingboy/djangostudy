from Qshop.views import app
from buyer import buyer_bl
from seller import seller_bl

app.register_blueprint(seller_bl, url_prefix="/seller")
app.register_blueprint(buyer_bl, url_prefix="/buyer")

if __name__ == '__main__':
    app.run(debug=True)
