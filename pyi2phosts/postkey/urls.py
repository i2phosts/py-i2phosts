from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.addkey, name='postkey-views-addkey'),
        url(r'^success/', views.success),
        url(r'^subdomain/', views.subdomain),
]
