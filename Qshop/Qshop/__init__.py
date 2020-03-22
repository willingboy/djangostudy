from flask import Flask

app = Flask(__name__,static_url_path="/static/",static_folder="../static",template_folder="../templates")
app.config.from_object("settings.Config")

