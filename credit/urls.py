from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.credit, name='creditpage'),
]

app_name = 'credit'