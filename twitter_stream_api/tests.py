from django.contrib.gis.geos import GEOSGeometry
from twython import Twython
from twitter_stream_api.models import MonitorTwitter, GeoTwitter
import datetime


def collect_monitor_twitter():

    a_date_time_now = datetime.datetime.now()

    all_MonitorTwitter= MonitorTwitter.objects.filter(initial_date__lte=a_date_time_now , final_date__gte=a_date_time_now)

    for monitor_twitter in all_MonitorTwitter:

        collect_twitters(args=[monitor_twitter.id])

def twitter(monitor_twitter):
    twitter = Twython(monitor_twitter.app_key(), monitor_twitter.app_secret(), oauth_version=2)
    monitor_twitter.set_acess_token(twitter.obtain_access_token())
    twitter = Twython(monitor_twitter.app_key(), access_token=monitor_twitter.access_token)
    return twitter

def collect_twitters(monitorTwitter_id):
    try:
        monitor_twitter = MonitorTwitter.objects.get(id=monitorTwitter_id)

    except MonitorTwitter.DoesNotExist:
        return

    items = twitter(monitor_twitter).search(q=monitor_twitter.search_term, result_type='recent', count=100, since_id=monitor_twitter.since_id)
    if items:
        for item in items['statuses']:
            geo_twitter = GeoTwitter()
            geo_twitter.monitor_twitter = monitor_twitter
            geo_twitter.twitter_id = item['id']
            geo_twitter.twitter_text= item['text']
            geo_twitter.sender_id = item['user']['id']
            geo_twitter.sender_screen_name = item['user']['screen_name']
            geo_twitter.sender_name = item['user']['name']
            geo_twitter.sender_avatar = item['user']['profile_image_url']
            if item['geo']: geo_twitter.geom = GEOSGeometry((item['geo']).__repr__())
            geo_twitter.save()

        monitor_twitter.last_searched_date = datetime.datetime.now()
        monitor_twitter.since_id = items['search_metadata']['max_id']
        monitor_twitter.save()
