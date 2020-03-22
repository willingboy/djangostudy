from Qshop import app
from Qshop.buyer import buyer_bl
from Qshop.models import db
from Qshop.seller import seller_bl

app.config.from_object("Qshop.settings.Config")
app.register_blueprint(seller_bl, url_prefix="/seller")
app.register_blueprint(buyer_bl, url_prefix="/buyer")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
