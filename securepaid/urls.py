from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^standard', views.index, name='index'),
    url(r'^generateQRcode', views.generateQRcode, name='generateQRcode'),

]
