import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskshop"
    static_url_path = "/static/"
    static_folder = os.path.join(BASE_DIR, "static")
    template_folder = os.path.join(BASE_DIR, "templates")
    debug = True
