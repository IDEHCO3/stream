from django.shortcuts import render


from django.views.generic import  TemplateView
#from twitter_stream_rest.models import MonitorTwitter, GeoTwitter, AccountTwitter

# Create your views here.
class MonitorTwitterView(TemplateView):
    model = None
    template_name = 'twitter_stream_view/main/index.html'
