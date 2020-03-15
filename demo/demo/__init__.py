from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from demo.settings import *

app = Flask(
    import_name=__name__,
    static_url_path=STATIC_URL,
    static_folder=STATICFILE_DIR,
    template_folder=TEMPLATE_DIR
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)



