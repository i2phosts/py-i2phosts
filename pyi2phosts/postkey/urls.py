from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.addkey, name='postkey-views-addkey'),
        url(r'^success/', views.success, name='postkey-views-success'),
        url(r'^subdomain/', views.subdomain, name='postkey-views-subdomain'),
]
