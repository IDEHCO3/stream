from django.conf.urls import include, patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from twitter_stream_api import views


urlpatterns = format_suffix_patterns([
    url(r'^user_name/account-twitter/$', views.AccountTwitterDetail.as_view(), name='account-twitter-list'),
    url(r'^monitors-twitters/$', views.MonitorTwitterList.as_view(), name='monitor-twitter-list'),
    url(r'^monitors-twitters/(?P<monitor_name>.*)$/', views.MonitorTwitterDetail.as_view(), name='monitor-twitter'),
    url(r'^monitors-twitters/(?P<monitor_name>.*)/geotwitters/$', views.GeoTwitterListFiltered.as_view(), name='geotwitter-monitor-twitter'),
    url(r'^monitors-twitters/(?P<monitor_name>.*)/geotwitters/(?P<attributes_functions>.*)/$', views.GeoTwitterListFiltered.as_view(), name=''),
    url(r'^(?P<user_name>.*)/monitors-twitters/$', views.MonitorTwitterListFiltered.as_view(), name='monitor-twitter-list-filtered'),
    url(r'^(?P<user_name>.*)/monitors-twitters/(?P<monitor_name>.*)/geotwitters/$', views.GeoTwitterListFiltered.as_view(), name='monitor-twitter-list-filtered'),
    url(r'^(?P<user_name>.*)/monitors-twitters/(?P<monitor_name>.*)/geotwitters/(?P<attributes_functions>.*)/$', views.GeoTwitterListFiltered.as_view(), name=''),
    url(r'^(?P<user_name>.*)/monitors-twitters/(?P<monitor_name>.*)/$', views.MonitorTwitterDetail.as_view(), name='monitor-twitter-list-filtered'),

])
