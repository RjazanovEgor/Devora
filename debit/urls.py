from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.debit, name='debitpage'),
]

app_name = 'debit'