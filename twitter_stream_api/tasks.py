from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from celery import task
from django.contrib.gis.geos import GEOSGeometry
from twython import Twython
from twitter_stream_api.models import MonitorTwitter, GeoTwitter
import datetime

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(minute='*/1')), ignore_result=True)
def monitor_twitter():

    a_date_time_now = datetime.datetime.now()
    #all_MonitorTwitter= MonitorTwitter.objects.filter(initial_date__lte=a_date_time_now , final_date__gte=a_date_time_now)
    all_MonitorTwitter= MonitorTwitter.objects.all()

    for monitor_twitter in all_MonitorTwitter:
        collect_twitters(monitor_twitter.id)

#@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def twitt_py(monitorTwitter):
    twitter = Twython(monitorTwitter.app_key(), monitorTwitter.app_secret(), oauth_version=2)
    monitorTwitter.set_acess_token(twitter.obtain_access_token())
    twitter = Twython(monitorTwitter.app_key(), access_token=monitorTwitter.access_token)
    return twitter

#@periodic_task(run_every=(crontab(minute='*/1')), ignore_result=True)
def collect_twitters(monitorTwitter_id):
    try:
        monitorTwitter = MonitorTwitter.objects.get(id=monitorTwitter_id)

    except MonitorTwitter.DoesNotExist:
        return
    twittpy = twitt_py(monitorTwitter)
    items = twittpy.search(q=monitorTwitter.search_term, result_type='recent', count=100, since_id=monitorTwitter.since_id)
    if items:
        for item in items['statuses']:
            geo_twitter = GeoTwitter()
            geo_twitter.monitor_twitter = monitorTwitter
            geo_twitter.twitter_id = item['id']
            geo_twitter.twitter_text= item['text']
            geo_twitter.sender_id = item['user']['id']
            geo_twitter.sender_screen_name = item['user']['screen_name']
            geo_twitter.sender_name = item['user']['name']
            geo_twitter.sender_avatar = item['user']['profile_image_url']
            if item['geo']: geo_twitter.geom = GEOSGeometry(to_geojson((item['geo'])))
            geo_twitter.save()

        monitorTwitter.last_searched_date = datetime.datetime.now()
        monitorTwitter.since_id = items['search_metadata']['max_id']
        monitorTwitter.save()

def to_geojson(geom):
    long = geom['coordinates'][1]
    lat = geom['coordinates'][0]
    geom['coordinates'][0] = long
    geom['coordinates'][1] = lat
    return geom.__repr__()
