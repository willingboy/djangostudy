import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskshop"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "aseiofe"  # 这是存储session要用到的密钥串
    debug = True
