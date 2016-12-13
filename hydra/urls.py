
from django.conf.urls import  url,include
from hydra.views import HydraVocab

urlpatterns = [
    url(r'^vocab/$', HydraVocab.as_view(), name="hydravocab"),
]

def getHydraVocabURLPatterns(inicialURL):
    return url(inicialURL, include('hydra.urls', namespace='hydra'))