from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.garant, name='garantpage'),
]

app_name = 'garant'