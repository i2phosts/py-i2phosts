from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^([^$/]+)', views.jumper, name='jump-views-jumper'),
        url(r'', views.index, name='jump-views-index'),
]
