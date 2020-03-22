from flask import Blueprint

buyer_bl = Blueprint("buyer", __name__)


@buyer_bl.route("/")
def index():
    return "buyer auth"
