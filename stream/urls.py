"""stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from hydra.urls import getHydraVocabURLPatterns

urlpatterns = [
    url(r'^stream/twitter/', include('twitter_stream_api.urls', namespace='twitter_stream_api')),
    url(r'^stream/view/streams/twitter/', include('twitter_stream_view.urls', namespace='twitter_stream_view')),
    url(r'^stream/twitter/contexts/', include('context_api.urls', namespace='context')),
    getHydraVocabURLPatterns(r'^streams/twitter/hydra/'),
]

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]