from demo import app
from demo import views


def path(url_view: dict):
    for k, v in url_view.items():
        v = app.route(k)(v)


urlpatterns = {
    "/": views.index,
    "/index.html": views.index,
    "/courses/index.html": views.courses_index,
}

path(url_view=urlpatterns)
