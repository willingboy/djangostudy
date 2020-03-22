from django.urls import path, re_path

from . import views

urlpatterns = [
    path('index.html', views.index),
    re_path('^$', views.index),
    path('list.html', views.listpage),
    path('detail.html', views.detail),
    path('cart.html', views.cart),
    path('place_order.html', views.place_order),
    path('user_center_site.html', views.user_center_site),
    path('user_center_info.html', views.user_center_info),
    path('user_center_order.html',views.user_center_order),
    path('alipay', views.alipay)
]
