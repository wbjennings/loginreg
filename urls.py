from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^loginreg$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success)
]