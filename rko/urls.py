from django.conf.urls import url, include
from . import views
from home import views as hv


urlpatterns = [
    url(r'^$', views.rko, name='rkopage'),
]

app_name = 'rko'
