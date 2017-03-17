from django.conf.urls import include, patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from twitter_stream_view.views import MonitorTwitterView


urlpatterns = format_suffix_patterns([

    url(r'^monitors-twitters/?$', MonitorTwitterView.as_view(), name='monitors-twitters-view'),


])
