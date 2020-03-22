from flask import Blueprint

seller_bl = Blueprint("seller", __name__)


@seller_bl.route("/")
def index():
    return "seller index"
