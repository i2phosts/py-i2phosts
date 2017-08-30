from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^all/$', views.all),
        url(r'^status/$', views.status),
]
