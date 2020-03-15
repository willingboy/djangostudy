import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_URL = '/static/'
STATICFILE_DIR = os.path.join(BASE_DIR, "static")

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/flaskdemo"
