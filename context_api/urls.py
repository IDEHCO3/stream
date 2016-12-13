
from django.conf.urls import  url
from context_api import views


urlpatterns = [
    url(r'^(?P<classname>.+)\.jsonld$', views.ContextView.as_view(), name='detail'),
    url(r'^(?P<classname>.+)\.jsonld#(?P<properties>)$', views.ContextView.as_view(), name='detail-property'),

]